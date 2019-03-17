import sys
from spellchecker import Spellchecker
from spellchecker.utils import words_from_file, normalize, highlight_incorrect


if __name__ == "__main__":
    spellchecker = Spellchecker()

    if len(sys.argv) > 2 and (sys.argv[1] in ['--file', '-f']):
        spellchecker.load(words_from_file(sys.argv[2]))

    while True:
        user_input = input('Please type a word or text: ')

        if user_input.strip() != '':
            maybe_text = user_input.split(' ')

            if len(maybe_text) > 1:
                wrong = spellchecker.check_list(words=list(map(normalize, maybe_text)))
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
                if spellchecker.check(word=normalize(user_input)):
                    print('The word is correct.')
                else:
                    suggestions = spellchecker.suggest(word=normalize(user_input))
                    if len(suggestions) > 0:
                        print('Did you mean:')
                        for suggestion in suggestions:
                            print(suggestion)
                    else:
                        print('No suggestions for this word.')
