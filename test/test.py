import data
data.p[2] = 2
print(data.p)
file_ = open('data.py', 'w')
file_.write('p = '+str(data.p))
file_.close
