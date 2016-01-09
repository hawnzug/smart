# Smartsegmentation

## Yet another Chinese word segmentation in Python
Final project of this semester.

This project is cooperated by **Chaoran Xu**, **Pihe Hu**, and **Zhuyang Wang**.

## Install and Run
Dependence: PyQt4

GUI: `main.py`

Or you can just `import segment` and use the function `main(string)`

## GUI
Using PyQt4

## Algorithm
Two algorithms are combined to implement the final segmentation.

The first one, written by Pihe Hu, is a system called [MMSEG](http://technology.chtsai.org/mmseg/).

When the **MMSEG** system encounters words that don't exist in the lexicon, it cuts the words off and sends them to the
second part, written by Zhuyang Wang. 

The second part is based on **HMM**(Hidden Markov Model) and **Viterbi** algorithm.

## Lexicon
The HMM model and initial lexicon is from [结巴中文分词](https://github.com/fxsjy/jieba).

Recently expand the lexicon from [Here](http://download.csdn.net/detail/logken/3575376).

The lexicon is written by Zhuyang Wang.

Combine 10+ different lexicons together into a file `dict.txt`.

`dict.txt` has two columns, the first is words or single character, the second is the corresponding probability.

We use **Trie**, which is also called prefix tree, to store the lexicon.

In Trie, all the descendants of a node have a common prefix associated with that
node, and the root is associated with the empty string. And every node stores
one Chinese character, while every leaf stores a number, which is exactly the
value of its prefix.
