# -*- coding: utf-8 -*-
from hmm import prob_emit
from hmm import prob_start
from hmm import prob_trans


PROB_START = prob_start.P
PROB_TRANS = prob_trans.P
PROB_EMIT = prob_emit.P
MINPROB = -3.14e+100


def init_array(x, y):
    array = []
    for i in range(x):
        array.append([])
        for j in range(y):
            array[i].append(0)
    return array


def viterbi(sentence):
    length = len(sentence)
    weight = init_array(length, 4)
    path = init_array(length, 4)
    for i in range(4):
        weight[0][i] = PROB_START[i] + PROB_EMIT[i].get(sentence[0], MINPROB)
    for i in range(1, length):
        for j in range(4):
            weight[i][j] = MINPROB
            path[i][j] = -1;
            p_emit = PROB_EMIT[j].get(sentence[i], MINPROB)
            for k in range(4):
                temp = weight[i-1][k]+PROB_TRANS[k][j]+p_emit
                if temp > weight[i][j]:
                    weight[i][j] = temp
                    path[i][j] = k
    if weight[length-1][1] > weight[length-1][3]:
        pos = 1
    else:
        pos = 3
    label = []
    table = ['B','E','M','S']
    for i in range(length-1, -1, -1):
        label.append(table[pos])
        pos = path[i][pos]
    return ''.join(label[::-1])


def output(line):
    split_line = ['']
    if line == '': return split_line
    label = viterbi(line)
    j = 0
    for i in range(len(line)):
        split_line[j] += line[i]
        if label[i] in ['E', 'S']:
            j += 1
            split_line.append('')
    return split_line[:-1]
