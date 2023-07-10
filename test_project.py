import pytest

from project import validate_url, validate_format, validate_quality, validate_outfile


def test_validate_url():
    assert validate_url("http://www.youtube.com/watch?v=OvKCESUCWII")
    assert validate_url("https://www.youtube.com/watch?v=OvKCESUCWII")
    assert validate_url("www.youtube.com/watch?v=OvKCESUCWII")
    assert validate_url("youtube.com/watch?v=OvKCESUCWII")
    assert validate_url("https://www.youtube.com/watch?v=OvKCESUCWII&t=30s")
    assert validate_url("https://youtu.be/OvKCESUCWII")

    with pytest.raises(SystemExit):
        assert validate_url("https://github.com/Sn1F3rt")

    with pytest.raises(SystemExit):
        assert validate_url("https:/www.youtube.com/watch?v=OvKCESUCWII")

    with pytest.raises(SystemExit):
        assert validate_url("https://www.youtube.com/watch?v=OVKCESUCWII")


def test_validate_format():
    assert validate_format("mp3")
    assert validate_format("mp4")

    with pytest.raises(SystemExit):
        assert validate_format("webm")

    with pytest.raises(SystemExit):
        assert validate_format("cat")


def test_validate_quality():
    assert validate_quality("720p", ["144p", "240p", "480p", "720p"])

    with pytest.raises(SystemExit):
        assert validate_quality("720p", ["144p", "240p", "480p"])

    with pytest.raises(SystemExit):
        assert validate_quality("cat", ["144p", "240p", "480p", "720p"])


def test_validate_outfile():
    assert validate_outfile("")
    assert validate_outfile("media")
    assert validate_outfile("audio.mp3")
    assert validate_outfile("video.mp4")

    with pytest.raises(SystemExit):
        assert validate_outfile("abc.123")

    with pytest.raises(SystemExit):
        assert validate_outfile("#vibe.mp3")
