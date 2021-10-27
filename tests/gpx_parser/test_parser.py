import os

from gpx_parser.parser.gpx_file_parser import GPXFileParser


def test_parser():
    GPXFileParser().parse("README.md")
