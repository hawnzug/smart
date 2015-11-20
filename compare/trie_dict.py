trie = {}
def trie_add(word, prob):
    ref = trie
    for char in word:
        if char not in ref:
            ref[char] = {}
        ref = ref[char]
    ref[''] = prob


def trie_search(word):
    ref = trie
    for char in word:
        if char not in ref:
            return False
        ref = ref[char]
    return True


f = open('dict.txt', 'r')
for line in f.readlines():
    word, prob = line.split()[:2]
    trie_add(word, prob)
print(trie)

#print(trie_search('哈'))
#print(trie_search('妈'))
#print(trie_search('呵呵'))
#print(trie_search('整数'))
#print(trie_search('电脑'))
