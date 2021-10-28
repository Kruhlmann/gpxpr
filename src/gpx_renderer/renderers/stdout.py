import sys
from typing import Iterator

from gpx_parser.parser.gpx_track_interval import GPXInterval
from gpx_renderer.renderer import Renderer
from gpx_renderer.terminal_colors import TerminalColors


class STDOUTRenderer(Renderer):
    def _color_from_pace(self, pace: float) -> TerminalColors:
        if pace > self._running:
            return TerminalColors.FAIL
        if pace > self._walking:
            return TerminalColors.WARNING
        return TerminalColors.OKCYAN

    def render(self, intervals: Iterator[GPXInterval]) -> None:
        for interval in intervals:
            color = self._color_from_pace(interval.speed_kmtime)
            sys.stdout.write(f"{color}█{TerminalColors.ENDC}")
