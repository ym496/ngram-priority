# Ngram-Priority
## Overview

The is a Python script that utilizes the [Google Books Ngram Viewer](https://books.google.com/ngrams/info) to analyze the relative popularity of words based on their occurrence in a large corpus of books over time. I wrote this to determine the priority of learning new words from my extensive list of new vocabulary. 

## Usage

To run the script, use the following command in your terminal:

```bash
python script.py "word1, word2, word3, ..."
```
Replace "word1, word2, word3, ..." with your list of words separated by commas.

## Example
```bash
$ python script.py "portmanteau,elucidated,unscrupulous,voraciously"

1. unscrupulous
2. elucidated
3. portmanteau
4. voraciously
```
## Dependencies
- Make sure to get Python 3.10.12 or higher.
- Install the dependencies.
```bash
pip install -r requirements.txt
```
