from io import TextIOWrapper
import os

from gpx_parser.io.file.file_is_not_a_file_error import FileIsNotAFileError
from gpx_parser.io.file.invalid_file_persmission_error import InvalidFilePermissionError


class FileHandle:
    def __init__(self, path: str, *permissions: int):
        self._check_path_exists(path)
        self._check_path_is_file(path)
        self._check_path_permissions(path, *permissions)
        self._source: TextIOWrapper = open(path)

    def close(self):
        self._source.close()

    @property
    def lines(self) -> list[str]:
        return self._source.readlines()

    @property
    def content(self) -> str:
        return self._source.read()

    def _check_path_exists(self, path: str) -> None:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Unable to find file {path}")

    def _check_path_is_file(self, path: str) -> None:
        if not os.path.isfile(path):
            raise FileIsNotAFileError(f"Item at {path} is not a file")

    def _check_path_permissions(self, path: str, *permissions: int) -> None:
        if not os.access(path, *permissions):
            permissions_as_strings = map(
                lambda permission_int: str(permission_int), permissions
            )
            access_flags = " &".join(permissions_as_strings)
            raise InvalidFilePermissionError(
                f"File {path} did not have permissions {access_flags}"
            )
