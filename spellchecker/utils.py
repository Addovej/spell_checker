import os


def words_from_os() -> [str]:
    if os.name in ['posix']:
        with open('/usr/share/dict/words') as words:
            return [normalize(word) for word in words]
    return []


def words_from_file(file: str) -> [str]:
    words = []
    try:
        with open(file) as file:
            for line in file:
                words += line.split(' ')
        words = list(map(normalize, words))
    except Exception as e:
        print(highlight_incorrect(str(e)))
    return words


def normalize(string: str) -> str:
    return string.lower().strip()


def highlight_incorrect(string: str) -> str:
    return '\33[31m{}\33[0m'.format(string)
