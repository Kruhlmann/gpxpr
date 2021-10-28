import sys
from typing import Iterator

from gpx_parser.parser.gpx_track_interval import GPXInterval
from gpx_renderer.renderer import Renderer


class STDOUTRenderer(Renderer):
    def render(self, intervals: Iterator[GPXInterval]) -> None:
        for interval in intervals:
            if interval.speed_kmtime < self._walking:
                sys.stdout.write("█")
            else:
                sys.stdout.write("x")
