import datetime
import sys
from typing import Any, Iterator, Optional

from matplotlib.lines import Line2D
from matplotlib import pyplot

from gpx_parser.parser.gpx_track_interval import GPXInterval
from gpx_renderer.line import Line
from gpx_renderer.renderer import Renderer
from gpx_renderer.vector import Vector


class MatplotLibRenderer(Renderer):
    def __init__(self, running: float, walking: float, destination: str):
        super().__init__(running=running, walking=walking, destination=destination)
        self._running_color = "green"
        self._walking_color = "orange"
        self._standing_color = "red"

    def _color_from_pace(self, pace: float) -> str:
        if pace < self._running:
            return self._running_color
        if pace < self._walking:
            return self._walking_color
        return self._standing_color

    def _compute_lines(
        self,
        intervals: Iterator[GPXInterval],
    ) -> Iterator[Line]:
        last_idx: int = 1
        last_vector: Optional[Vector] = None
        for interval in intervals:
            x1 = last_idx
            x2 = last_idx + int(interval.duration_s) + 1
            x = x2 - abs(x1 - x2) / 2
            y = min(interval.speed_kmtime, self._walking)
            color = self._color_from_pace(interval.speed_kmtime)
            current_vector = Vector(x, y)
            yield Line(
                start=last_vector or current_vector, end=current_vector, color=color
            )
            last_idx = x2
            last_vector = current_vector

    def _set_legend(self, axes: Any) -> None:
        custom_lines = [
            Line2D([0], [0], color=self._running_color, lw=4),
            Line2D([0], [0], color=self._walking_color, lw=4),
            Line2D([0], [0], color=self._standing_color, lw=4),
        ]
        axes.legend(custom_lines, ["Running", "Walking", "Standing"])

    def _set_axes_formatting(self, axes: Any) -> None:
        axes.xaxis.set_major_formatter(self._x_axis_formatter)
        axes.yaxis.grid(True)
        pyplot.xlabel("Time")
        pyplot.ylabel("Pace (min/km)")

    def _x_axis_formatter(self, seconds: int, _: Any) -> str:
        return str(datetime.timedelta(seconds=seconds))

    def render(self, intervals: Iterator[GPXInterval]) -> None:
        _, axes = pyplot.subplots(figsize=(30, 5))
        for line in self._compute_lines(intervals):
            p1 = [line.start.x, line.end.x]
            p2 = [line.start.y, line.end.y]
            axes.plot(p1, p2, color=line.color)
        self._set_legend(axes)
        self._set_axes_formatting(axes)
        pyplot.gca().invert_yaxis()
        pyplot.savefig(self._destination or sys.stdout)
