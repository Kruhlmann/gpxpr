import pytest

from gpx_renderer.factory import RendererFactory
from gpxpr.main import parse_and_render


def test_valid_arguments() -> None:
    for renderer in RendererFactory.RENDERERS:
        parse_and_render(
            [
                "-r",
                renderer,
                "tests/data/valid.gpx",
                "-w",
                "13.0",
                "-v",
                "7.5",
            ],
        )


def test_invalid_arguments() -> None:
    with pytest.raises(SystemExit):
        parse_and_render([])
