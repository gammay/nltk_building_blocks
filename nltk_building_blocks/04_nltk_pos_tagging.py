text = "Computers don't speak English. So, we've to learn C, C++, Java, Python and the like! Yay!"

import nltk
from nltk.tokenize import word_tokenize

words = word_tokenize(text)

pos_tagged_text = nltk.pos_tag(words)
print(pos_tagged_text)

nltk.help.upenn_tagset()

for pos_tag_word in pos_tagged_text:
    print(pos_tag_word[0], ":")
    nltk.help.upenn_tagset(pos_tag_word[1])

