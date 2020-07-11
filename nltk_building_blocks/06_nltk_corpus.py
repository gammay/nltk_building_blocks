# coding: utf-8
'''
Created on May 2, 2020

@author: GM
'''
import nltk
from nltk.corpus import CategorizedTaggedCorpusReader


def corpus_info(corpus):
    print(corpus)
    print()
    print("README:", corpus.readme())
    print()
    files = corpus.fileids()
    print(len(files), "files:")
    print(files)
    print()
    file = files[0]
    text = corpus.raw(file)
    print("File", file, len(corpus.paras(file)), "paras", len(corpus.sents(file)), "sentences", len(corpus.words(file)), "words", ":")
    print(text.encode("utf-8"))
    print()
    if isinstance(corpus, nltk.corpus.TaggedCorpusReader):
        tagged_words = corpus.tagged_words()
        print(len(tagged_words), "tags:")
        print(tagged_words)
        print()
    if isinstance(corpus, nltk.corpus.CategorizedTaggedCorpusReader):
        categories = corpus.categories()
        print(len(categories), "categories:")
        print(categories)
        print()
        category = categories[-1]
        files = corpus.fileids(category)
        print(len(files), "files in category", category, ":")
        print(files)
        print()
        file = files[0]
        print("File:", file, len(corpus.paras(file)), "paras", len(corpus.sents(file)), "sentences", len(corpus.words(file)), "words")
        print()
        print("Raw text:")
        text = corpus.raw(file)
        print(text)
        print()
        print("Tagged text:")
        tagged_words = corpus.tagged_words(file)
        print(tagged_words)
        print()

# corpus_info(nltk.corpus.abc)
corpus_info(nltk.corpus.brown)
# corpus_info(nltk.corpus.movie_reviews)
