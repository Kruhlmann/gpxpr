import sys
from typing import Iterator

from gpx_parser.parser.gpx_track_interval import GPXInterval
from gpx_renderer.renderer import Renderer
from gpx_renderer.terminal_colors import TerminalColors


class STDOUTRenderer(Renderer):
    def __init__(self, running: float, walking: float):
        super().__init__(running=running, walking=walking)
        self._running_color = TerminalColors.OKCYAN
        self._walking_color = TerminalColors.WARNING
        self._standing_color = TerminalColors.FAIL

    def _color_from_pace(self, pace: float) -> TerminalColors:
        if pace < self._running:
            return self._running_color
        if pace < self._walking:
            return self._walking_color
        return self._standing_color

    def _render_legend(self):
        sys.stdout.write(
            f"{self._standing_color}█{TerminalColors.ENDC}: Standing (pace is slower than {self._walking} min/km)\n",
        )
        sys.stdout.write(
            f"{self._walking_color}█{TerminalColors.ENDC}: Walking  (pace is between {self._walking} min/km and {self._running} min/km)\n",
        )
        sys.stdout.write(
            f"{self._running_color}█{TerminalColors.ENDC}: Running  (pace is faster than {self._running} min/km)\n",
        )

    def render(self, intervals: Iterator[GPXInterval]) -> None:
        self._render_legend()
        self._render_graph(intervals)

    def _render_graph(self, intervals: Iterator[GPXInterval]) -> None:
        for interval in intervals:
            number_of_seconds_active = range(int(interval.duration_s) + 1)
            for _ in number_of_seconds_active:
                color = self._color_from_pace(interval.speed_kmtime)
                sys.stdout.write(f"{color}█{TerminalColors.ENDC}")
