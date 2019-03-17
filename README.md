# Simple Spellchecker
## Requirements
Python 3
## Usage
Download
```commandline
git clone https://github.com/Addovej/spellchecker.git
cd spellchecker
```
```commandline
python3 main.py --file <path_to_file> (optional)

Please type a word or text: test
The word is correct.
Please type a word or text: merging
The word is correct.
Please type a word or text: hellwo
Did you mean:
hello
Please type a word or text: sometimes we can make a mistakse
sometimes we can make a *mistakse* 
{'mistakse': ['mistake']}
```
Run tests
```commandline
pytest -s -v tests/spellchecker.py
```
