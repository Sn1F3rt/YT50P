# Xolon

My **final project** for the **[CS50P](https://cs50.harvard.edu/python/2022/)** course! :sparkles::tada:

## Table of Contents

- [About](#about)
- [Demo](#demo)
- [Installation](#installation)
  * [Prerequisites](#prerequisites)
  * [Setup](#setup)
- [Running](#running)
- [License](#license)
  

## About

**YT50P** is a tool which helps download a YouTube video in **mp3/mp4**. It supports both library usage and a command line interface (CLI).

## Demo

Video demonstration of the tool: YOUTUBE_LINK

## Installation

### Prerequisites

The requirements for **YT50P** are as follows:

* `python3` (tested on **v3.11.2**)
* `git`

### Setup

Clone the GitHub repository:  
```shell
git clone https://github.com/Sn1F3rt/YT50P
```

Install the dependencies
```shell
python -m pip install -r requirements.txt
```

## Running

You can either run the script in interactive input mode `python project.py` or using the CLI:

```shell
(venv) PS P:\Python\YT50P> python project.py -h
usage: project.py [-h] [-u URL] [-f FORMAT] [-q QUALITY] [-o OUTFILE]

Download a Youtube video in mp4/mp3 format (both library and CLI usage supported)

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     The URL of the Youtube video
  -f FORMAT, --format FORMAT
                        The format of the output file (mp3/mp4)
  -q QUALITY, --quality QUALITY
                        The quality of the output video (only supported for mp4)
  -o OUTFILE, --outfile OUTFILE
                        The name of the output file

Thank you for choosing YT50P! <3
```

## License

[MIT License](LICENSE)

Copyright &copy; 2023 Sayan Bhattacharyya
