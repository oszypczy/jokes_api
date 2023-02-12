from jokes_io import (
    get_jokes,
    download_stop_words,
    Joke,
    write_to_json,
    calculate_word_count
)
from io import StringIO


def test_get_jokes():
    jokes = get_jokes()
    assert jokes[0].joke == 'Chuck Norris is the reason why Waldo is hiding.'
    assert jokes[0].num_of_words == 9


def test_download_stop_words():
    stop_words = download_stop_words()
    assert len(stop_words) == 127
    assert stop_words[0] == 'i'


def test_write_to_json():
    jokes = [Joke("Chuck Norris is the reason why Waldo is hiding")]
    handle = StringIO()
    write_to_json(handle, jokes)
    handle.seek(0)
    content = handle.read()
    assert content == '[\n  {\n    "9": [\n      "Chuck Norris is the reason why Waldo is hiding"\n    ]\n  }\n]' # noqa 551


def test_calculate_word_count():
    stop_words = download_stop_words()
    jokes = [Joke("Chuck Chuck is the reason Waldo Waldo Waldo is")]
    word_count = calculate_word_count(jokes, stop_words)
    word_count = sorted(word_count)
    assert word_count == [(1, 'reason'), (2, 'Chuck'), (3, 'Waldo')]
