import os

from gpx_parser.io.file.file import File
from gpx_parser.parser.parser import Parser


class GPXFileParser(Parser):
    def parse(self, filename: str) -> None:
        with File(filename, os.R_OK) as gpx_file:
            print(gpx_file.content)
