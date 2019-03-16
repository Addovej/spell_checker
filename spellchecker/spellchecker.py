from .trie import Trie
from .utils import words_from_os


class Spellchecker(object):

    def __init__(self):
        self.trie = Trie()
        self.load(words_from_os())

    def __contains__(self, item):
        return item in self.trie

    def load(self, words: list):
        try:
            for word in words:
                self.trie.append(word)
        except Exception as e:
            print('Oops, error is happened. Message: {}'.format(e))

    def check(self, word: str) -> bool:
        return word in self.trie

    def check_list(self, words: list) -> list:
        return [word for word in words if not self.check(word)]

    def suggest(self, word: [str], l_distance: int=1) -> [str]:
        def _suggest(node, char, prev_row):
            columns = len(word) + 1
            curr_row = [prev_row[0] + 1]

            for col in range(1, columns):
                insert = curr_row[col - 1] + 1
                delete = prev_row[col] + 1
                replace = prev_row[col - 1] if word[col - 1] == char else prev_row[col - 1] + 1

                curr_row.append(min(insert, delete, replace))

            if node.word and curr_row[-1] <= l_distance:
                results.append(node.word)

            if min(curr_row) <= l_distance:
                for char in node.children:
                    _suggest(node.children[char], char, curr_row)

        curr_row = range(len(word) + 1)

        results = []
        for child in self.trie.node.children:
            _suggest(self.trie.node.children[child], child, curr_row)

        return results

    def suggest_list(self, words: [str], l_distance: int=1) -> {str: [str]}:
        results = {}
        for word in words:
            results[word] = self.suggest(word, l_distance)

        return results
