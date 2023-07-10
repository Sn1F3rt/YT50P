import os
import re

import pytube

from constants import YT_REGEX, FILE_REGEX


class YT50P(pytube.YouTube):
    def __init__(
        self, url: str, fmt: str = None, quality: str = None, outfile: str = None
    ):
        self.url = url
        self.fmt = fmt
        self.quality = quality
        self.outfile = re.search(FILE_REGEX, outfile).group(1) if outfile else outfile

        super().__init__(url=url)

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url: str):
        if not self.validate(url):
            raise ValueError("Invalid Youtube video URL")

        self._url = url

    @staticmethod
    def validate(url: str):
        return re.search(YT_REGEX, url)

    def save(self):
        if self.fmt == "mp3":
            steam = self.streams.filter(only_audio=True).first()

        else:
            steam = self.streams.filter(progressive=True, res=self.quality).first()

        outfile = steam.download(output_path=".")

        if not self.outfile:
            self.outfile = self.video_id + f".{self.fmt}"

        else:
            self.outfile += f".{self.fmt}"

        os.rename(outfile, self.outfile)
