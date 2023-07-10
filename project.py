import re
import sys

from pytube.exceptions import VideoUnavailable


from constants import FILE_REGEX
from classes import YT50P


def validate_url(url: str):
    try:
        _ = YT50P(url=url).title

    except ValueError as e:
        sys.exit(str(e))

    except VideoUnavailable:
        sys.exit("Something went wrong with that video!")

    return True


def validate_format(fmt: str):
    if fmt not in ["mp3", "mp4"]:
        sys.exit("Invalid format")

    return True


def validate_quality(quality: str, available_qualities: list):
    if quality not in available_qualities:
        sys.exit("Invalid quality")

    return True


def validate_outfile(outfile: str):
    if not outfile:
        return True

    if not re.search(FILE_REGEX, outfile):
        sys.exit("Invalid output file name")

    return True


def main():
    from utils import parse_cli, interactive_input

    url, fmt, quality, outfile = parse_cli() or interactive_input()

    yt = YT50P(url=url, fmt=fmt, quality=quality, outfile=outfile)
    yt.save()

    print(f"Video title: {yt.title}")
    print(f"Saved file: {yt.outfile}")


if __name__ == "__main__":
    main()
