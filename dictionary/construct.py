# -*- coding: utf-8 -*-
TRIE = {}
def construct(txtfile='dict.txt', pyfile='dictionary.py'):
    file_ = open(txtfile, 'r')
    lines = file_.readlines()
    for line in lines:
        split_line = line.split()
        trie_add(split_line[0], int(split_line[1]))
    file_.close()
    file_ = open(pyfile, 'w')
    file_.write('TRIE = '+str(TRIE))
    file_.close


def trie_add(word, prob):
    ref = TRIE
    for char in word:
        if char not in ref:
            ref[char] = {}
        ref = ref[char]
    ref[''] = prob


if __name__ == '__main__':
    construct()
