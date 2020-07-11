import nltk

stemmer = nltk.stem.PorterStemmer()

word = "building"
print("Stem of", word, ':', stemmer.stem(word))

lemmatizer = nltk.stem.WordNetLemmatizer()

word = "building"
pos = 'n';
print("Lemmatization of", word, "(" , pos, "):", lemmatizer.lemmatize(word, pos))
pos = 'v';
print("Lemmatization of", word, "(" , pos, "):", lemmatizer.lemmatize(word, pos))

