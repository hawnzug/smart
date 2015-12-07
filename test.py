import viterbi.test


def output(line):
    split_line = ['']
    if line == '': return split_line
    label = viterbi.test.viterbi(line)
    j = 0
    for i in range(len(line)):
        split_line[j] += line[i]
        if label[i] in ['E', 'S']:
            j += 1
            split_line.append('')
    return split_line


def test(filename):
    SPLIT_PUNCS = ['，', '。', '？', '！', '…', '：', '（', '）']
    def no_split_punc(line):
        for i in range(len(line)):
            if line[i] in SPLIT_PUNCS:
                return i
        return -1
    input_file = open(filename, 'r')
    lines = []
    while True:
        line = input_file.readline()
        if not line:
            newline = ''.join(lines)
            print(output(newline))
            break
        line = line.strip().replace('\n', '')
        pos = no_split_punc(line)
        lines.append(line)
        while pos != -1:
            line = lines[-1][pos:]
            lines[-1] = lines[-1][:pos]
            newline = ''.join(lines)
            print(output(newline))
            print(line[0])
            line = line[1:]
            lines = [line]
            pos = no_split_punc(line)


if __name__ == '__main__':
    test('input')
