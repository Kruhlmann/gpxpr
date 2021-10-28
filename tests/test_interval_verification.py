import pytest

from gpx_parser.parser.gpx_parse_error import GPXParseError
from gpx_parser.parser.gpx_track_interval import GPXInterval
from tests.mock.point import MockPoint


def test_interval_verification() -> None:
    valid_point = MockPoint(0, 0, 0)
    invalid_time_point = MockPoint(None, 0, 0)
    invalid_speed_point = MockPoint(0, "a", 0)
    invalid_distance_point = MockPoint(0, 0, pytest)

    GPXInterval.from_point_pair(valid_point, valid_point)
    with pytest.raises(GPXParseError):
        GPXInterval.from_point_pair(invalid_time_point, valid_point)
    with pytest.raises(GPXParseError):
        GPXInterval.from_point_pair(invalid_speed_point, valid_point)
    with pytest.raises(GPXParseError):
        GPXInterval.from_point_pair(invalid_distance_point, valid_point)
