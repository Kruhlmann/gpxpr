import sys
from typing import Any, Iterator, Optional

from matplotlib import pyplot
import numpy

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
            y = min(interval.speed_kmtime, 40)
            color = self._color_from_pace(interval.speed_kmtime)
            current_vector = Vector(x, y)
            yield Line(
                start=last_vector or current_vector, end=current_vector, color=color
            )
            last_idx = x2
            last_vector = current_vector

    def _set_axis_aspect_ration(self, axis: Any, ratio: float) -> None:
        x_left, x_right = axis.get_xlim()
        y_low, y_high = axis.get_ylim()
        axis.set_aspect(abs((x_right - x_left) / (y_low - y_high)) * ratio)

    def render(self, intervals: Iterator[GPXInterval]) -> None:
        _, ax = pyplot.subplots(figsize=(30, 5))
        for line in self._compute_lines(intervals):
            p1 = [line.start.x, line.end.x]
            p2 = [line.start.y, line.end.y]
            ax.plot(p1, p2, color=line.color)
        pyplot.gca().invert_yaxis()
        pyplot.savefig(self._destination or sys.stdout)
