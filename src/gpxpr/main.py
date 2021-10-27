from gpx_parser.gpx_parser import parse_gpx_file
from gpx_renderer.gpx_renderer import render_gpx_parse


def main():
    parse_gpx_file()
    render_gpx_parse()


if __name__ == "__main__":
    main()
