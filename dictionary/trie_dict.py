# -*- coding: utf-8 -*-
import dictionary
TRIE = dictionary.TRIE


def trie_add(word, prob):
    ref = TRIE
    for char in word:
        if char not in ref:
            ref[char] = {}
        ref = ref[char]
    ref[''] = prob


def trie_delete(word):
    ref = TRIE
    if trie_search(word):
        for char in word:
            if len(ref[char]) == 1:
                del ref[char]
                return True
            else:
                ref = ref[char]
    else:
        return False


def trie_search(word):
    ref = TRIE
    for char in word:
        if char not in ref:
            return False
        else:
            ref = ref[char]
    if '' not in ref:
        return False
    else:
        return ref['']


def dict_update(filename='dictionary.py'):
    file_ = open(filename, 'w')
    file_.write('TRIE = '+str(TRIE))
    file_.close
