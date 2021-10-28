import sys
from typing import Iterator

from matplotlib import pyplot
import numpy

from gpx_parser.parser.gpx_track_interval import GPXInterval
from gpx_renderer.renderer import Renderer


class MatplotLibRenderer(Renderer):
    def _compute_coordinates(
        self,
        intervals: Iterator[GPXInterval],
    ) -> Iterator[tuple[tuple[int, float], tuple[int, float]]]:
        last_idx: int = 1
        for interval in intervals:
            duration_in_seconds = int(interval.duration_s) + 1
            x1 = last_idx
            x2 = last_idx + duration_in_seconds
            y = min(interval.speed_kmtime, 40)
            yield ((x1, y), (x2, y))
            last_idx = x2

    def render(self, intervals: Iterator[GPXInterval]) -> None:
        times: list[int] = []
        paces: list[float] = []
        for coordinate in self._compute_coordinates(intervals):
            times.append(numpy.median(coordinate[0][0]))
            times.append(numpy.median(coordinate[1][0]))
            paces.append(numpy.mean(coordinate[0][1]))
            paces.append(numpy.mean(coordinate[1][1]))
        pyplot.gca().invert_yaxis()
        pyplot.plot(times, paces, "-")
        pyplot.savefig(self._destination or sys.stdout)
