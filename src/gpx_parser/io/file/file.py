from typing import Iterable, Optional

from gpx_parser.io.device import Device
from gpx_parser.io.file.handle import FileHandle


class File(Device):  # noqa: WPS110
    def __init__(self, path: str, *permissions: int):
        self._path: str = path
        self._permissions: Iterable[int] = permissions
        self._file_handle: Optional[FileHandle] = None

    def __enter__(self) -> FileHandle:  # noqa: D105
        self._file_handle = FileHandle(self._path, *self._permissions)
        return self._file_handle

    def __exit__(self, *_) -> None:  # type: ignore # noqa: D105
        if self._file_handle is None:
            return
        self._file_handle.close()
        self._file_handle = None
