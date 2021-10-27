from gpx_parser.parser.gpx_file_parser import GPXFileParser


def test_valid_file():
    intervals = list(GPXFileParser("tests/data/valid.gpx").parse())
    assert len(intervals) == 2
    assert intervals[0].speed_ms * intervals[0].duration_s == intervals[0].distance_m
