TRIE = {}
def construct():
    file_ = open('dict.txt', 'r')
    lines = file_.readlines()
    for line in lines:
        split_line = line.split()
        trie_add(split_line[0], int(split_line[1]))
    file_.close()
    file_ = open('dict.py', 'w')
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
