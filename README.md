# YT50P

My **final project** for the **[CS50P](https://cs50.harvard.edu/python/2022/)** course! :sparkles::tada:


## Table of Contents

- [About](#about)
- [Demo](#demo)
- [Installation](#installation)
  * [Prerequisites](#prerequisites)
  * [Setup](#setup)
- [Running](#running)
- [Documentation](#documentation)
- [License](#license)
  

## About

**YT50P** is a tool which helps download a YouTube video in **mp3/mp4**. It supports both library usage and a command line interface (CLI). Check [documentation](#documentation) for documentation on all of the available functionality.


## Demo

Video demonstration of the tool: **https://youtu.be/ftFMRgI6_TQ**


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


## Documentation

- `classes.py`\
  Houses the class `YT50P`, a subclass of `pytube.YouTube` with additional functionality. The URL is validated **for formatting** using the `validate()` method. The `save()` method saves the YouTube video/audio to local storage.
  
- `constants.py`\
  Defines the YouTube URL regex (`YT_REGEX`) and the output file name regex (`FILE_REGEX`).
  
- `utils.py`\
  Contains various utility and helper functions.
  * `get_available_qualities()` returns a sorted list of the available video qualities/resolutions for the given YouTube video URL.
  * `validate_params()` validates all the input parameters from the CLI. 
  * `parse_cli()` parses the CLI input parameters if provided using `argparse`.
  * `interactive_input()` launches an interactive input session for the user and validates parameters.
  
- `project.py`\
  Contains the core project functionality.
  * `validate_url()` validates the input URL using a preliminary regex and passes it to the `YT50P` class to check for `pytube.exceptions.VideoUnavailable` exception. 
  * `validate_format()` validates the format input parameter to be either `mp3` or `mp4`.
  * `validate_quality()` validates the input video quality against the available qualities for the input YouTube video URL.
  * `validate_outfile()` validates the output file name entered for discrepancies.
  * `main()` checks for CLI input parameters or launches an interactive session with the user. Finally, it prints the video title and the name of the saved file.
  
- `test_project.py`\
  Contains the tests for the `validate_*` functions from the `project.py` file.

> **NOTE:**  I've imported the `parse_cli()` and `interactive_input()` functions locally inside `main()` to prevent a circular import error, since these functions are defined in a separate file but depend on the functions defined inside the `project.py` file. For anyone wondering why I chose to retain the `validate_*` functions inside `project.py` even though I moved the rest of the functions to utils, the structuring of the final project requires me to have at least **3** custom functions in the `project.py` file.


## License

[MIT License](LICENSE)

Copyright &copy; 2023 Sayan Bhattacharyya
