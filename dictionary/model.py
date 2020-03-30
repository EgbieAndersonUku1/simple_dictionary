import json
from difflib import get_close_matches
from os import getcwd
from os.path import join


_DATA_JSON_PATH = join(getcwd(), 'dictionary', 'data.json')


class Dictionary(object):

    def __init__(self):
        self._data = None

    def load_json(self):
        """This loads the json file in the class"""
        self._data = json.load(open(_DATA_JSON_PATH))

    def translate(self, word):
        """translate(str) -> return str

           Takes a given word and then returns the meaning for the word
        """
        word_meaning = self._data.get(word.lower())

        if not word_meaning:
            word_meaning = self._data.get(word.title())
        if not word_meaning:
            word_meaning = self._data.get(word.upper())
        return word_meaning

    def get_best_matches(self, word):
        """get_best_matches(str) -> return str

           Takes a given word and returns all the words that are closest
           matches

           >>> get_best_matches("rain")
           ['rain', 'train', 'rainy']
        """
        return get_close_matches(word, self._data.keys(), cutoff=0.7)


