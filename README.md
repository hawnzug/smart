# Smartseg

## Yet another Chinese word segmentation in Python
Final project of Python(Unfinished).

This project is cooperated by Chaoran Xu, Pihe Hu, and Zhuyang Wang.

## Algorithm
Two algorithms are combined to implement the final segmentation.

The first one, written by Pihe Hu, is a system called [MMSEG](http://technology.chtsai.org/mmseg/).

When the MMSEG system encounters words that don't exist in the dictionary, it cuts the words off and sends them to the
second part, written by Zhuyang Wang. 

The second part is based on HMM(Hidden Markov Model) and Viterbi algorithm.

## Dictionary
The HMM model and initial dictionary is from [结巴中文分词](https://github.com/fxsjy/jieba).
Recently expand the dictionary from [Here](http://download.csdn.net/detail/logken/3575376). Now the dict has 665466 words.
