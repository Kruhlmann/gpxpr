import pytest

from gpxpr.main import parse_and_render


def test_valid_arguments() -> None:
    parse_and_render(
        [
            "-r",
            "STDOUTRenderer",
            "tests/data/valid.gpx",
            "-w",
            "13.0",
            "-v",
            "7.5",
            "-o",
            "/tmp/1.png",
        ],
    )
    parse_and_render(
        [
            "-r",
            "MatplotLibRenderer",
            "tests/data/valid.gpx",
            "-w",
            "13.0",
            "-v",
            "7.5",
            "-o",
            "/tmp/1.png",
        ],
    )


def test_invalid_arguments() -> None:
    with pytest.raises(SystemExit):
        parse_and_render([])
