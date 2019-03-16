import os


def words_from_os():
    if os.name in ['posix']:
        with open('/usr/share/dict/words') as words:
            return [word.lower().strip() for word in words]
    return []
