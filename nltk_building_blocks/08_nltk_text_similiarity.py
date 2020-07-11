from nltk.corpus import wordnet

# syn1 = wordnet.synsets('football', 'n')
# syn2 = wordnet.synsets('soccer', 'n')
syn1 = wordnet.synsets('code', 'n')
syn2 = wordnet.synsets('bug', 'n')

# A word may have multiple synsets, so need to compare each synset of word1 with synset of word2
for s1 in syn1:
    for s2 in syn2:
        print("Path similarity of: ")
        print(s1, '(', s1.pos(), ')', '[', s1.definition(), ']')
        print(s2, '(', s2.pos(), ')', '[', s2.definition(), ']')
        print("   is", s1.path_similarity(s2))
        print()
