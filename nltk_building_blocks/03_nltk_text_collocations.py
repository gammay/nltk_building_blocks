# coding: utf-8

import urllib.request

# Download text and decode
# Note: Set proxy if behind a proxy (https://docs.python.org/2/library/urllib.html)
url = "http://www.gutenberg.org/files/1342/1342-0.txt"
text = urllib.request.urlopen(url).read().decode()
print(text)

# Tokenize
from nltk.tokenize import word_tokenize
text = word_tokenize(text)

# Remove stopwords
from nltk.corpus import stopwords
stops = stopwords.words('english')
# print(stops)
words = [word for word in text if word not in stops]

# Remove punctuations
import string
punctuations = list(string.punctuation)
punctuations.append('\ufeff')
punctuations.append('“')
punctuations.append('”')
punctuations.append('’')
punctuations.append('\'\'')
print("Punctuations:", punctuations)

words = [word for word in words if word not in punctuations]
print("Preprocessed:", words)

# Bigrams
from nltk.metrics import BigramAssocMeasures
from nltk.collocations import BigramCollocationFinder
bigram_collocation = BigramCollocationFinder.from_words(words)
# Top 10 most occurring collocations
print("Bigrams:", bigram_collocation.nbest(BigramAssocMeasures.likelihood_ratio, 10))

# Trigrams
from nltk.collocations import TrigramCollocationFinder
from nltk.metrics import TrigramAssocMeasures
trigram_collocation = TrigramCollocationFinder.from_words(words)
# Top 10 most occurring collocations
print("Trigrams:", trigram_collocation.nbest(TrigramAssocMeasures.likelihood_ratio, 10))
