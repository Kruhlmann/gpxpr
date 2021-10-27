import sys

from gpx_parser.io.readable import Readable
from gpx_parser.io.writable import Writable


class STDIO(Writable, Readable):
    def write(self, buffer: str) -> int:
        return sys.stdout.write(buffer)

    def read(self) -> str:
        return sys.stdin.read()
