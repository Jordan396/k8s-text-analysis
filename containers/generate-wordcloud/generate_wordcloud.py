#!/usr/bin/env python

import time
import os
import json
from wordcloud import WordCloud, STOPWORDS

# Config variables
reduced_output_filename = os.environ['REDUCED_OUTPUT_FILENAME']
wordcloud_filename = os.environ['WORDCLOUD_FILENAME']

def main():
  with open(reduced_output_filename) as json_file:
    data = json.load(json_file)
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(width=900,height=500, stopwords=stopwords, max_words=1628,relative_scaling=1,normalize_plurals=False).generate_from_frequencies(data)
    wordcloud.to_file(wordcloud_filename)

if __name__ == "__main__": 
  main()