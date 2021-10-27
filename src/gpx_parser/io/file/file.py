from typing import Iterable, Optional

from gpx_parser.io.device import Device
from gpx_parser.io.file.handle import FileHandle


class File(Device):
    def __init__(self, path: str, *permissions: int):
        self._path: str = path
        self._permissions: Iterable[int] = permissions
        self._file_handle: Optional[FileHandle] = None

    def __enter__(self) -> FileHandle:
        self._file_handle = FileHandle(self._path, *self._permissions)
        return self._file_handle

    def __exit__(self, *_) -> None:
        if self._file_handle is None:
            return
        self._file_handle.close()
        self._file_handle = None
