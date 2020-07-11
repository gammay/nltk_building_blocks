"""
Created on May 10, 2020

@author: GM
"""
import nltk
from gmpycommon.gmutils import dprint
from nltk.corpus import wordnet
from pprint import pprint


def synset_info(synset):
    print("Name", synset.name())
    print("POS:", synset.pos())
    print("Definition:", synset.definition())
    # print("Examples:", synset.examples())
    print("Lemmas:", synset.lemmas())
    print("Antonyms:", [lemma.antonyms() for lemma in synset.lemmas() if len(lemma.antonyms()) > 0])
    print("Hypernyms:", synset.hypernyms())
    print("Instance Hpernyms:", synset.instance_hypernyms())
    print("Part Holonyms:", synset.part_holonyms())
    print("Part Meronyms:", synset.part_meronyms())
    print()

synsets = wordnet.synsets('code')
# synsets = wordnet.synsets('computer')
# synsets = wordnet.synsets('encode')
# synsets = wordnet.synsets('sleep')
# synsets = wordnet.synsets('window')
# synsets = wordnet.synsets('hot')

print(len(synsets), 'synsets:')
for synset in synsets: synset_info(synset)

def hypernyms(synset):
    return synset.hypernyms()

synsets = wordnet.synsets('code')
for synset in synsets:
    print(synset.name() + " tree:")
    pprint(synset.tree(rel=hypernyms))
    print()

#
# print('Name:', synsets[0].name())
# print('POS:', synsets[0].pos())
# print('Definition:', synsets[0].definition())
# print('Examples:', synsets[0].examples())
#
# lemmas = synsets[1].lemmas()
# for lemma in synsets[1].lemmas():
#     print(lemma, ':', lemma.name())
# print(len(lemmas), 'lemma(s):', lemmas)
# for lemma in lemmas:
#     print(lemma.lemmas())
# synset_of_lemma = lemmas[1].synset()
# print(synset_of_lemma)

# print('Name:', synsets[1].name())
# print('POS:', synsets[1].pos())
# print('Definition:', synsets[1].definition())
# print('Examples:', synsets[1].examples())

# pprint("-Hypernyms:------------------")
# pprint(code_v_01.hypernyms())
# pprint("-Tree of Hypernyms:----------")
# pprint(code_v_01.tree(rel_hypernyms))
# pprint("-Tree of Lemmas:----------")
# pprint(code_v_01.tree(rel_lemmas))
# pprint("-----------------------------")

# pprint(synset_info(synsets[1].lemmas()[0].synset()))
# nltk.corpus.reader.wordnet.Lemma

# 
# print("'", word, "'", " (", pos, ")", " has ", len(synsets), " synsets:", sep="")
# for i, synset in zip(range(len(synsets)), synsets):
#     print("Synset", i, ":")
#     synset_info(synset)
#     print()
