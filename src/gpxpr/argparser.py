import argparse


class GPXPRArgParserFactory:
    @staticmethod
    def create_argparser() -> argparse.ArgumentParser:  # noqa: WPS605,WPS602
        argparser = argparse.ArgumentParser()
        argparser.add_argument(
            "-r",
            "--renderer",
            required=True,
            type=str,
            help="Renderer to use",
            action="store",
            dest="renderer",
        )
        argparser.add_argument(
            "-o",
            "--output",
            required=False,
            type=str,
            help="Output location. Default is /dev/stdout",
            action="store",
            dest="output",
        )
        argparser.add_argument(
            "target",
            type=str,
            help="File to process",
            action="store",
        )
        return argparser
