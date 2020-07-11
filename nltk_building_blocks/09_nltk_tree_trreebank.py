# coding: utf-8
'''
Created on May 2, 2020

@author: GM
'''
from pprint import pprint

import nltk

text = "I love open source"
# Tokenize to words
words = nltk.tokenize.word_tokenize(text)
# POS tag the words
words_tagged = nltk.pos_tag(words)
# A simple grammar to create tree
grammar = "NP: {<JJ><NN>}"
# Create tree
parser = nltk.RegexpParser(grammar)
tree = parser.parse(words_tagged)
pprint(tree)

tree.draw()

words = nltk.corpus.treebank.words()
print(len(words), "words:")
print(words)

tagged_sents = nltk.corpus.treebank.tagged_sents()
print(len(tagged_sents), "sentences:")
print(tagged_sents)

sent0 = tagged_sents[0]
pprint(sent0)

grammar = '''
    Subject: {<NNP><NNP>}
    SubjectInfo: {<CD><NNS><JJ>}
    Action: {<MD><VB>}
    ActionInfo: {<NNP><CD>}
    Object: {<DT><NN>}
    ObjectInfo: {<JJ><NN>}
    Stopwords: {<IN><DT>}
'''
parser = nltk.RegexpParser(grammar)
tree = parser.parse(sent0)
print(tree)

tree.draw()

