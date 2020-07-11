text = "Computers don't speak English. So, we've to learn C, C++, ,C#, Java, Python and the like! Yay!"

from nltk.tokenize import sent_tokenize
sentences = sent_tokenize(text)
print(len(sentences), 'sentence(s): ', sentences)

from nltk.tokenize import word_tokenize
words = word_tokenize(text)
print(len(words), 'word(s): ', words)

text = "I love nltk.org"

from nltk.tokenize import sent_tokenize
sentences = sent_tokenize(text)
print(len(sentences), 'sentence(s): ', sentences)

from nltk.tokenize import word_tokenize
words = word_tokenize(text)
print(len(words), 'word(s): ', words)
