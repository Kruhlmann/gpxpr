import pytest

from gpxpr.main import parse_and_render


def test_valid_arguments() -> None:
    parse_and_render(["-r", "tst", "tests/data/valid.gpx"])


def test_invalid_arguments() -> None:
    with pytest.raises(SystemExit):
        parse_and_render([])
