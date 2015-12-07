# -*- coding: utf-8 -*-
import smalltrie_dict
TRIE = smalltrie_dict.TRIE


def trie_add(word, prob):
    ref = TRIE
    for char in word:
        if char not in ref:
            ref[char] = {}
        ref = ref[char]
    ref[''] = prob


def trie_search(word):
    ref = TRIE
    for char in word:
        if char not in ref:
            return False
        ref = ref[char]
    if '' not in ref:
        return False
    else:
        return ref['']


def trie_delete(word):
    ref = TRIE
    if trie_search(word):
        for char in word:
            if len(ref[char]) == 1:
                del ref[char]
                break
            ref = ref[char]


def dict_update():
    file_ = open('dict_data.py', 'w')
    file_.write('TRIE = '+str(TRIE))
    file_.close
