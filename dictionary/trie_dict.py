# -*- coding: utf-8 -*-
import dictionary
TRIE = dictionary.TRIE


def trie_add(word, prob):
    '''Add word, probability into the dictionary and return True.
If the word already exists in the dictionary, return False.'''
    ref = TRIE
    if trie_search(word) == -1:
        for char in word:
            if char not in ref:
                ref[char] = {}
            ref = ref[char]
        ref[0] = prob
        return True
    else:
        return False


def trie_delete(word):
    '''Delete word, probability from the dictionary and return True.
If the word doesn't exist in the dictionary, return False.'''
    if trie_search(word) != -1:
        ref = TRIE
        for char in word:
            if len(ref[char]) == 1:
                del ref[char]
                return True
            else:
                ref = ref[char]
        return True
    else:
        return False


def trie_search(word):
    '''Search a certain word.
If exists, return its probability.
If not, return False.'''
    ref = TRIE
    for char in word:
        if char not in ref:
            return -1
        else:
            ref = ref[char]
    if 0 not in ref:
        return -1
    else:
        return ref[0]


def list_all():
    result = []
    word = []
    def recursive(ref):
        for char in ref:
            if char == 0:
                result.append(''.join(word))
            else:
                word.append(char)
                recursive(ref[char])
                del word[-1]
    recursive(TRIE)
    return result


def dict_update(filename='dictionary.py'):
    '''Update the dictionary, store it in dictionary.py.'''
    file_ = open(filename, 'w')
    file_.write('TRIE = '+str(TRIE))
    file_.close
