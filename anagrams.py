#!/usr/bin/env python

import sys
import string
import itertools

anagrams = {}

corpus = sys.stdin.read().lower()

# brute force split punctuation
non_letters = set(c for c in corpus if c not in string.letters)
for c in non_letters:
    corpus = corpus.replace(c, ' ')
words = [w for w in set(x for x in corpus.split() if len(x) >= 4)]

word_pairs = set()
for i, word1 in enumerate(words):
    for word2 in words[i+1:]:
        word_pairs.add((word1, word2))

for word1, word2 in word_pairs:
    key = ''.join(sorted('%s%s' % (word1, word2)))
    existing_words = anagrams.get(key, [])
    word_list = [(word1, word2)]
    flat = []
    for pair in existing_words:
        [flat.append(x) for x in pair]
    if existing_words:
        if word1 not in flat and word2 not in flat:
            word_list.extend((existing_words))
        else:
            word_list = existing_words
    anagrams[key] = word_list

longest = max(len(x) for x in anagrams.values())
print 'Longest is %d pairs long' % longest

for matches in anagrams.values():
    if len(matches) < longest:
        continue
    print ', '.join((' '.join(word_set)) for word_set in matches)
