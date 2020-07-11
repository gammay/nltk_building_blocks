
sentence = "Peterson first suggested the name 'open source' at Palo Alto, California"

import nltk

words = nltk.word_tokenize(sentence)
pos_tagged = nltk.pos_tag(words)

ne_tagged = nltk.ne_chunk(pos_tagged)
print("NE tagged text:")
print(ne_tagged)
print()

print("Recognized named entities:")
for ne in ne_tagged:
    if hasattr(ne, "label"):
        print(ne.label(), ne[0:])

ne_tagged.draw()
