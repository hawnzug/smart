f = open('dict.txt', 'r')
trie = {}
for line in f.readlines():
    word = line.split()[0]
    for ch in range(len(word)):
        wfrag = word[:ch+1]
        if wfrag not in trie:
            trie[wfrag] = 0
        
print(trie)
