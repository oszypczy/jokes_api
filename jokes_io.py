import json
from matplotlib import pyplot as plt
import string
import requests


def download_jokes():
    jokes = []
    for _ in range(50):
        joke = requests.get('https://geek-jokes.sameerkumar.website/api?format=json').json() # noqa 551
        try:
            jokes.append(joke['joke'] + '\n')
        except KeyError:
            continue
    with open('jokes.txt', 'r') as handle:
        handle.writelines(jokes)


def get_jokes():
    with open('jokes.txt', 'r') as handle:
        jokes = handle.readlines()
    return [Joke(joke) for joke in jokes]


def download_stop_words():
    with open('stop_words.txt', 'r') as handle:
        stop_words = handle.readlines()
    return [word.rstrip() for word in stop_words]


def write_to_json(handle, jokes):
    data = []
    set_of_lenghts = set([joke.num_of_words for joke in jokes])
    for lenght in set_of_lenghts:
        values = []
        values = [str(joke) for joke in jokes if joke.num_of_words == lenght]
        joke_data = {lenght: values}
        data.append(joke_data)
    json.dump(data, handle, indent=2)


def calculate_word_count(jokes, stop_words):
    words = []
    for each_joke in jokes:
        for word in str(each_joke).split(' '):
            if word.lower() not in stop_words:
                words.append(word.rstrip(string.punctuation))
    final_list = []
    for each_word in set(words):
        final_list.append((words.count(each_word), each_word))
    return final_list


def draw_length_plot(jokes):
    x = list(set([joke.num_of_words for joke in jokes]))
    y = []
    for each_length in x:
        y.append(len([joke for joke in jokes if joke.num_of_words < each_length])) # noqa 551
    plt.plot(x, y, 'o')
    plt.xlabel(xlabel="Number of words")
    plt.ylabel(ylabel="Jokes not longer than x")
    plt.title(label='Jokes length')
    plt.savefig('jokes_length.jpg')


def draw_word_count_plot(data):
    words = [tup[0] for tup in data]
    frequency = [tup[1] for tup in data]
    plt.bar(frequency, words, color="green", label="words")
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.xticks(rotation=30, color='teal', size=12)
    plt.yticks(color='teal', size=12)
    plt.title('Bar plot')
    plt.legend()
    plt.savefig("jokes_words.jpg")


class Joke:
    def __init__(self, joke):
        joke = joke.rstrip()
        self.joke = joke
        self.num_of_words = len(joke.split(' '))

    def __str__(self) -> str:
        return self.joke
