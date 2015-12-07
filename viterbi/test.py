import numpy
import viterbi.prob_emit
import viterbi.prob_start
import viterbi.prob_trans


PROB_START = numpy.array(viterbi.prob_start.P)
PROB_TRANS = numpy.array(viterbi.prob_trans.P)
PROB_EMIT = viterbi.prob_emit.P
MINPROB = -3.14e+100


def viterbi(sentence):
    length = len(sentence)
    weight = numpy.zeros((length, 4))
    path = numpy.zeros((length, 4))
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
        label.append(table[int(pos)])
        pos = path[i][pos]
    return ''.join(label[::-1])



