file_ = open('dict.txt', 'r')
result = 0
for line in file_:
    result += int(line.split()[1])
print(result)
file_.close
