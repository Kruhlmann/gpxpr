import sys
from typing import Iterator

from matplotlib import pyplot

from gpx_renderer.renderer import Renderer


class MatplotLibRenderer(Renderer):
    def render(self, _: Iterator) -> None:

        # Create data
        x = range(1, 6)
        y = [1, 4, 6, 8, 4]

        # Area plot
        pyplot.fill_between(x, y)
        pyplot.savefig(self._destination or sys.stdout)
