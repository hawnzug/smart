# -*- coding: utf-8 -*-
import lexicon
import math
TRIE = lexicon.TRIE

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
        for i, char in enumerate(word):
            if len(ref[char]) == 1:
                del ref[char]
                return True
            elif i == len(word)-1:
                del ref[char][0]
                return True
            else:
                ref = ref[char]
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
    a=open('read.txt',"r")
    while True:
        b=a.readline()
        if len(b)==0:
            break
        t+=b.replace("\n"," ").replace(" ","")
    a.close()
    return t

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
        if trie_search(chunk[len(chunk)-i-1:])!=-1:
            if complex_match(chunk[:len(chunk)-i-1],[chunk[len(chunk)-i-1:]]+result)==True:
                temp.append([chunk[len(chunk)-i-1:]]+result)

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

def count_word(dic):
    count=0
    for i in dic.keys():
        if i==0:
            count+=dic[0]
        else:
            count+=count_word(dic[i])
    return count

items=count_word(TRIE)


def sum__word_frequency(list):
    result=0
    for i in list:
        result+=math.log10(trie_search(i)/items)
    return result

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
    result=temp+result
    chunk=chunk[:len(chunk)-len_list(temp)]
    return mmseg_chunk(chunk,result)

def text_to_chunk(text):
    result=[]
    temp=''
    for i in text:
        if trie_search(i)!=-1:
            temp+=i
        else:
            if temp!='':
                result.append(temp)
                temp=''
            if i!='—':
                result.append(i)
            else:
                if len(result)==0 or result[len(result)-1]!=i:
                    result.append(i)
                else:
                    result[len(result)-1]=i+i
    if temp not in result and temp!='':
        result.append(temp)
    return result

def text_to_sentence(text):
    result=[]
    temp=''
    for i in text:
        if i!='。':
            temp+=i
        else:
            if temp!='':
                result.append(temp+i)
                temp=''
    if temp not in result and temp!='':
        result.append(temp)
    return result

def main(text):
    result=[]
    seg_text=text_to_sentence(text)
    for i in seg_text:
        sentence=text_to_chunk(i)
        seg_sentence=[]
        for i in sentence:
            if len(i)!=-1 and trie_search(i[0])!=-1:
                seg_sentence+=mmseg_chunk(i,[])
            else:
                seg_sentence.append(i)
        result.append(seg_sentence)
    return result
