from nltk.corpus import stopwords

stop_words = stopwords.words('english')
print(len(stop_words), " stopwords:", stop_words)

text = "Computers do not speak English. So, we have to learn C, C++, Java, Python and the like! Yay!"

from nltk.tokenize import word_tokenize
words = word_tokenize(text)

print(len(words), "words in original text:", words)
words = [word for word in words if word not in stop_words]
print(len(words), "words without stopwords:", words)

import string
punctuations = list(string.punctuation)
print(punctuations)

words = [word for word in words if word not in punctuations]
print(len(words), "words without stopwords and punctuations:", words)
