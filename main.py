from spellchecker import Spellchecker


def normalize(string: str):
    return string.lower().strip()


def highlight_incorrect(string: str) -> str:
    return '\33[31m{}\33[0m'.format(string)


if __name__ == "__main__":
    spellchecker = Spellchecker()

    while True:
        user_input = input('Please type a word or text: ')
        maybe_text = user_input.split(' ')

        if len(maybe_text) > 1:
            wrong = spellchecker.check_list(maybe_text)
            if len(wrong) > 0:
                output = ''
                for word in maybe_text:
                    output += '{} '.format(highlight_incorrect(word) if word in wrong else word)
                print(output)

                result = spellchecker.suggest_list(words=list(map(normalize, wrong)))
                print(result)
            else:
                print('Your text is correct.')
        else:
            if spellchecker.check(word=user_input):
                print('The word is correct.')
            else:
                suggestions = spellchecker.suggest(word=normalize(user_input))
                if len(suggestions) > 0:
                    print('Did you mean:')
                    for suggestion in suggestions:
                        print(suggestion)
                else:
                    print('No suggestions for this word.')
