# -*- coding: utf-8 -*-
import mmseg
from hmm import hmm
PUNCS = '。《，》？/·「」：；‘’“”|、{}`～！@#￥……&×（）-——=+\n'
ALPHA = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUM = '0123456789'
HANNUM = '零一二两三四五六七八九十百千万亿兆几.%'
CUTTING = '极是比于在由从给到不没未了过着的地得这那其第来去很都刚和与及而向之乎哉也所啊吗吧啦呀么你我他上下左右又'


def special_dealing(chars, next_word):
    result = []
    buf = []
    end_with_alpha = False

    def dealing(buf):
        if buf != []:
            result.extend(hmm.output(''.join(buf)))

    for char in chars:
        if char in CUTTING:
            dealing(buf)
            result.append(char)
            buf = []
        else:
            if char in ALPHA:
                if not end_with_alpha:
                    end_with_alpha = True
                    dealing(buf)
                    buf = []
            elif end_with_alpha:
                result.append(''.join(buf))
                buf = []
                end_with_alpha = False
            buf.append(char)
    if end_with_alpha:
        result.append(''.join(buf))
    elif buf != []:
        result.extend(hmm.output(''.join(buf)))
    return result


def main(lines):
    final = []
    for line in mmseg.main(lines):
        buf = []
        result = []
        end_with_num = False
        for word in line:
            if end_with_num:
                i = 0
                while i < len(word):
                    if word[i] in HANNUM or word[i] in NUM or word[i] == '点':
                        buf[-1] += word[i]
                        i += 1
                    else:
                        break
                if i < len(word):
                    result.extend(buf)
                    result.append(word[i:])
                    buf = []
                    end_with_num = False
            elif len(word) == 1 and word not in PUNCS and word not in NUM and word not in HANNUM:
                buf.append(word)
            else:
                if len(buf) <= 1:
                    result.extend(buf)
                else:
                    result.extend(special_dealing(buf, word))
                buf = []
                if len(word) == 1 and (word in NUM or word in HANNUM):
                    end_with_num = True
                    buf.append(word)
                else:
                    result.append(word)
        if len(buf) <= 1:
            result.extend(buf)
        else:
            result.extend(special_dealing(buf, word))
        final.extend(result)
    return final


if __name__ == '__main__':
    test()
