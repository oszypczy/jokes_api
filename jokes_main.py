import sys
import argparse
from jokes_io import (
    get_jokes,
    write_to_json,
    draw_length_plot,
    download_stop_words,
    calculate_word_count,
    draw_word_count_plot
)


def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument("--write_to_json", action='store_true')
    parser.add_argument("--draw_length_plot", action='store_true')
    parser.add_argument("--draw_word_count_plot", action='store_true')
    args = parser.parse_args(arguments[1:])
    jokes = get_jokes()
    if args.write_to_json:
        with open('jokes_by_length.json', 'w') as handle:
            write_to_json(handle, jokes)
    if args.draw_length_plot:
        draw_length_plot(jokes)
    if args.draw_word_count_plot:
        stop_words = download_stop_words()
        words = calculate_word_count(jokes, stop_words)
        words = sorted(words, reverse=True)
        draw_word_count_plot(words[:10])


if __name__ == "__main__":
    main(sys.argv)
