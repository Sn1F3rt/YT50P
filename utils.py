import argparse

from classes import YT50P
from project import validate_url, validate_format, validate_quality, validate_outfile


def get_available_qualities(url: str):
    yt = YT50P(url)

    qualities = set()

    for stream in yt.streams.filter(progressive=True):
        qualities.add(stream.resolution)

    return sorted(qualities, reverse=True, key=lambda x: int(x.split("p")[0]))


def validate_params(**kwargs):
    validate_url(url=kwargs["url"])
    validate_format(fmt=kwargs["fmt"])

    if kwargs["fmt"] == "mp4":
        validate_quality(
            quality=kwargs["quality"],
            available_qualities=get_available_qualities(kwargs["url"]),
        )

    validate_outfile(outfile=kwargs["outfile"])


def parse_cli():
    parser = argparse.ArgumentParser(
        description="Download a Youtube video in mp4/mp3 format (both library and CLI usage supported)",
        epilog="Thank you for choosing YT50P! <3",
    )
    parser.add_argument(
        "-u", "--url", default="", help="The URL of the Youtube video", type=str
    )
    parser.add_argument(
        "-f",
        "--format",
        default="mp4",
        help="The format of the output file (mp3/mp4)",
        type=str,
    )
    parser.add_argument(
        "-q",
        "--quality",
        default="",
        help="The quality of the output video (only supported for mp4)",
        type=str,
    )
    parser.add_argument(
        "-o", "--outfile", default="", help="The name of the output file", type=str
    )
    args = parser.parse_args()

    if not args.url:
        return False

    validate_params(
        url=args.url, fmt=args.format, quality=args.quality, outfile=args.outfile
    )

    # noinspection PyUnresolvedReferences
    return args.url, args.format, args.quality, args.outfile


def interactive_input():
    url = input("Video URL: ")
    validate_url(url=url)

    fmt = input("Format (mp4/mp3): ")
    validate_format(fmt=fmt)

    if fmt == "mp4":
        qualities = get_available_qualities(url=url)
        print(f"Available Qualities: {' | '.join(qualities)}")

        quality = input("Quality: ")
        validate_quality(quality=quality, available_qualities=qualities)

    else:
        quality = None

    outfile = input("Output file name: ")
    validate_outfile(outfile)

    return url, fmt, quality, outfile
