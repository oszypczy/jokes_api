README for Jokes-API

Introduction:
This is a Python script that analyzes jokes and generates useful insights from them. The script downloads 50 jokes from an API, stores them in a .txt file, and then analyzes the jokes. The analysis includes:
- Writing jokes to a JSON file grouped by their length
- Plotting a graph showing the distribution of jokes' length
- Plotting a bar graph showing the most frequent words used in the jokes (excluding stop words)

Requirements:
- python 3.x
- matplotlib
- requests
- json

Usage:
The script can be run from the command line with the following arguments:
--write_to_json: writes the jokes to a JSON file
--draw_length_plot: plots a graph showing the distribution of jokes' length
--draw_word_count_plot: plots a bar graph showing the most frequent words used in the jokes (excluding stop words)

Example:
css
Copy code
python jokes_analyzer.py --write_to_json --draw_length_plot --draw_word_count_plot

Results:
jokes_by_length.json file containing the jokes grouped by their length
jokes_length.jpg file showing the distribution of jokes' length
jokes_words.jpg file showing the most frequent words used in the jokes (excluding stop words)

Note:
The stop_words.txt file contains a list of common English stop words and the jokes.txt file will be created when the script is run.
