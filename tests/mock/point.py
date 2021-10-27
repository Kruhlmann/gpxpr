from typing import Any

from gpx_parser.geometry.point import Point


class MockPoint(Point):
    def __init__(
        self,
        duration_difference: Any,
        speed_difference: Any,
        distance_difference: Any,
    ):
        self._duration_difference: Any = duration_difference
        self._speed_difference: Any = speed_difference
        self._distance_difference: Any = distance_difference

    def time_difference(self, _: Point) -> Any:
        return self._duration_difference

    def distance_2d(self, _: Point) -> Any:
        return self._distance_difference

    def speed_between(self, _: Point) -> Any:
        return self._speed_difference
