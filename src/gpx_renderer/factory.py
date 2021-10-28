from typing import Type

from gpx_renderer.renderer import Renderer
from gpx_renderer.renderer_not_found_error import RendererNotFoundError
from gpx_renderer.renderers.stdout import STDOUTRenderer


class RendererFactory:
    RENDERERS: dict[str, Type[Renderer]] = {  # noqa: WPS115
        "STDOUTRenderer": STDOUTRenderer,
    }

    @staticmethod
    def renderer_from_string(  # noqa: WPS602
        renderer: str,
        running: float,
        walking: float,
    ) -> Renderer:
        if renderer not in RendererFactory.RENDERERS.keys():
            raise RendererNotFoundError(f"No such renderer {renderer}.")
        return RendererFactory.RENDERERS[renderer](running=running, walking=walking)
