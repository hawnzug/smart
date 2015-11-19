import numpy
import prob_emit
import prob_start
import prob_trans


p_start = numpy.array(prob_start.P)
p_trans = numpy.array(prob_trans.P)


def viterbi(sentence):
    """TODO: Docstring for viterbi.

    :sentence: TODO
    :returns: TODO

    """
    MINPROB = -3.14e+100
    length = len(sentence)
    weight = numpy.zeros((length, 4))
    path = numpy.zeros((length, 4))

    for i in range(4):
        weight[0][i] = p_start[i] + prob_emit.P[i].get(sentence[0], MINPROB)

    for i in range(1, length):
        for j in range(4):
            weight[i][j] = MINPROB
            path[i][j] = -1;
            p_emit = prob_emit.P[j].get(sentence[i], MINPROB)
            for k in range(4):
                temp = weight[i-1][k]+p_trans[k][j]+p_emit
                if temp > weight[i][j]:
                    weight[i][j] = temp
                    path[i][j] = k

    if weight[length-1][1] > weight[length-1][3]:
        pos = 1
    else:
        pos = 3

    label = ''
    a = ['B','E','M','S']
    for i in range(length-1, -1, -1):
        label += a[int(pos)]
        pos = path[i][pos]

    return label[::-1]


def main(filename):
    """TODO: Docstring for input.

    :filename: TODO
    :returns: TODO

    """
    input_file = open(filename, 'r')
    line = input_file.readline().strip()
    while line:
        label = viterbi(line)
        for i in range(len(line)):
            print(line[i], end='')
            if label[i] in ['E', 'S']:
                print(' ', end='')
        print('')
        line = input_file.readline().strip()


main('input')
