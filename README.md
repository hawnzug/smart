# Smartsegmentation

## Yet another Chinese word segmentation in Python
Final project of this semester(Unfinished).

This project is cooperated by **Chaoran Xu**, **Pihe Hu**, and **Zhuyang Wang**.

## Algorithm
Two algorithms are combined to implement the final segmentation.

The first one, written by Pihe Hu, is a system called [**MMSEG**](http://technology.chtsai.org/mmseg/).

When the **MMSEG** system encounters words that don't exist in the lexicon, it cuts the words off and sends them to the
second part, written by Zhuyang Wang. 

The second part is based on **HMM**(Hidden Markov Model) and **Viterbi** algorithm.

## Lexicon
The HMM model and initial lexicon is from [**结巴中文分词**](https://github.com/fxsjy/jieba).
Recently expand the lexicon from [**Here**](http://download.csdn.net/detail/logken/3575376).

The lexicon used by MMSEG is written by Zhuyang Wang.
Until now the lexicon has 665466 words.
First I combined 10+ different lexicons together into a file **dict.txt**.

**dict.txt** has two columns, the first is words or single character, the second is the corresponding probability.
Since MMSEG system only needs the probability of one single character,
so the probability of the word more than 2 characters is set to 0.

Then it is stored in a Python's dictionary named TRIE. Because the final lexicon is stored in a special data structure
called Trie(前缀树), which can undermine the total size of the lexicon.

In Trie, a vertex represents a single character, and all the words that begin with this character is stored under this
Trie recursively.

For example......
