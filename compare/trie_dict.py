# -*- coding: utf-8 -*-
import dict_data
TRIE = dict_data.TRIE


def trie_add(word, prob):
    ref = TRIE
    for char in word:
        if char not in ref:
            ref[char] = {}
        ref = ref[char]
    ref[''] = prob


def dict_update():
    file_ = open('dict_data.py', 'w')
    file_.write('TRIE = '+str(TRIE))
    file_.close


def trie_search(word):
    ref = TRIE
    for char in word:
        if char not in ref:
            return False
        ref = ref[char]
    return ref['']
