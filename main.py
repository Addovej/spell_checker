from spellchecker import Spellchecker


def normalize(word: str):
    return word.lower().strip()


if __name__ == "__main__":
    spellchecker = Spellchecker()

    while True:
        user_input = input('Please type a word or text: ')
        maybe_text = user_input.split(' ')

        if len(maybe_text) > 1:
            result = spellchecker.suggest_list(words=list(map(normalize, maybe_text)))

            print(result)
        else:
            result = spellchecker.suggest(word=normalize(user_input))

            if result['correct']:
                print('The word is correct.')
            elif len(result['suggestions']) > 0:
                print('Did you mean:')
                for suggestion in result['suggestions']:
                    print(suggestion)
            else:
                print('No suggestions for this word.')
