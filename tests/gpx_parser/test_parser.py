from gpx_parser.parser.gpx_file_parser import GPXFileParser

ACCEPTABLE_ERROR_THRESHOLD = 0.1


def test_valid_file() -> None:
    intervals = list(GPXFileParser("tests/data/valid.gpx").parse())
    assert len(intervals) == 2
    for interval in intervals:
        expected_distance_m = interval.speed_ms * interval.duration_s
        distance_delta = abs(expected_distance_m - interval.distance_m)
        assert distance_delta < ACCEPTABLE_ERROR_THRESHOLD
