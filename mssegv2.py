# -*- coding: utf-8 -*-
import resultA
import math

TRIE = resultA.TRIE


def trie_add(word, prob):
    ref = TRIE
    if trie_search(word) == -1:
        for char in word:
            if char not in ref:
                ref[char] = {}
            ref = ref[char]
        ref[0] = prob
        return True
    else:
        return False


def trie_delete(word):
    if trie_search(word) != -1:
        ref = TRIE
        for char in word:
            if len(ref[char]) == 1:
                del ref[char]
                return True
            else:
                ref = ref[char]
        return True
    else:
        return False


def trie_search(word):
    ref = TRIE
    for char in word:
        if char not in ref:
            return -1
        else:
            ref = ref[char]
    if 0 not in ref:
        return -1
    else:
        return ref[0]


def list_all():
    result = []
    word = []
    def recursive(ref):
        for char in ref:
            if char == 0:
                result.append(''.join(word))
            else:
                word.append(char)
                recursive(ref[char])
                del word[-1]
    recursive(TRIE)
    return result


def dict_update(filename='dictionary.py'):
    file_ = open(filename, 'w')
    file_.write('TRIE = '+str(TRIE))
    file_.close


def read():
    t=""
    a=open("read.txt","r")
    while True:
        b=a.readline()
        if len(b)==0:
            break
        t+=b.replace("\n"," ").replace(" ","")
    a.close()
    return t


def complex_max_match(list):
    max_match=[]
    for i in list:
        for k in range(len(i[2])):
            temp_string_list=i[:2]+[i[2][:k+1]]
            count=0
            for j in temp_string_list:
                if trie_search(j)!=-1:
                    count+=1
            if count==3:
                max_match.append(temp_string_list)
    return max_match

def average_word_length(list):
    sum=0
    for i in list:
        sum+=len(i)
    average_length=sum/len(list)
    return average_length

def variance_of_word_lengths(list):
    average_length=average_word_length(list)
    variance=0
    for i in list:
        variance+=(len(i)-average_length)**2/3
    return variance


def complex_match(chunk,result):
    if len(result)==3:
        return True
    if len(chunk)==0:
        return True
    for i in range(len(chunk)):
        if trie_search(chunk[:i+1])!=-1:
            if complex_match(chunk[i+1:],result+[chunk[:i+1]])==True:
                temp.append(result+[chunk[:i+1]])

def len_list(list):
    string=''
    for i in list:
        string+=i
    return len(string)

def largest_len(list):
    max=list[0]
    result=[]
    for i in list:
        if len_list(i)>len_list(max):
            max=i
            result=[]
        elif len_list(i)==len_list(max) and i!=max:
            result.append(i)
    result.append(max)
    return result

def largest_average_length(list):
    max=list[0]
    result=[]
    for i in list:
        if average_word_length(i)>average_word_length(max):
            max=i
            result=[]
        elif average_word_length(i)==average_word_length(max) and i!=max:
            result.append(i)
    result.append(max)
    return result


def smallest_variance(list):
    smallest=list[0]
    result=[]
    for i in list:
        if variance_of_word_lengths(i)<variance_of_word_lengths(smallest):
            smallest=i
            result=[]
        elif (variance_of_word_lengths(i)==variance_of_word_lengths(smallest)
              and i!=smallest):
            result.append(i)
    result.append(smallest)
    return result

def count_sigle_word(dic):
    count=0
    for i in dic.keys():
        count+=int(dic[i].get(0,0))
    return count

def cal_log(char):
    if trie_search(char)!=-1:
        return math.log10(trie_search(char)/items)

def sum__word_frequency(list):
    result=0
    for i in list:
        if len(i)==1:
            result+=cal_log(i)
    if result!=0:
        return result
    return math.log10(0.00001/items)

def largest_frequency(list):
    max=list[0]
    result=[]
    for i in list:
        if sum__word_frequency(i)>sum__word_frequency(max):
            max=i
            result=[]
        elif sum__word_frequency(i)==sum__word_frequency(max) and i!=max:
            result.append(i)
    result.append(max)
    return result


def mmseg(chunk):
    global temp
    temp=[]
    complex_match(chunk,[])
    temp1=largest_len(temp)
    if len(temp1)==1:
        return temp1[0]
    else:
        temp2=largest_average_length(temp1)
        if len(temp2)==1:
            return temp2[0]
        else:
            temp3=smallest_variance(temp2)
            if len(temp3)==1:
                return temp3[0]
            else:
                return largest_frequency(temp3)[0]

def mmseg_chunk(chunk,result):
    if chunk=='':
        return result
    temp=mmseg(chunk)
    result+=temp
    chunk=chunk[len_list(temp):]
    return mmseg_chunk(chunk,result)

def phragraph_to_sentence(pragraph):
    result=[]
    temp=''
    for i in pragraph:
        temp+=i
        if i=="。":
            result.append(temp[:len(temp)-1])
            temp=''
    return result

def sentence_to_chunk(sentence):
    sentence+='。'
    result=[]
    temp1=''
    temp2=''
    for i in sentence:
        if trie_search(i)!=-1:
            temp1+=i
            if temp2!='':
                result.append(temp2)
            temp2=''
        else:
            temp2+=i
            if temp1!='':
                result.append(temp1)
            temp1=''
    return result

def mmseg_main(phragraph):
    result=[]
    sentences=phragraph_to_sentence(phragraph)
    for i in sentences:
        sentence=sentence_to_chunk(i)
        for i in sentence:
            if trie_search(i[0])!=-1:
                result+=mmseg_chunk(i,[])
            else:
                result.append(i)
            result.append('。')
    return result

def main(string):
    list=mmseg_main(string)
    result=''
    for i in list:
        result+=i+"|"
    return result
items=count_sigle_word(TRIE)
