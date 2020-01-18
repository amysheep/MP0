import random 
import os
import string
import sys

stopWordsList = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
            "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its",
            "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
            "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
            "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
            "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
            "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
            "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
            "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
            "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

delimiters = " \t,;.?!-:@[](){}_*/"

def getIndexes(seed):
    random.seed(seed)
    n = 10000
    number_of_lines = 50000
    ret = []
    for i in range(0,n):
        ret.append(random.randint(0, 50000-1))
    return ret

def split_to_words(sentences):
    word_list = []
    for sentence in sentences:
        for i in delimiters:
            sentence = sentence.replace(i, ' ')
        for word in sentence.split(' '):
            if word and word.lower() not in stopWordsList:
                word_list.append(word.lower())
    return word_list

def process(userID):
    indexes = getIndexes(userID)
    ret = []
    # TODO
    # read in txt
    sublines = [
        line.strip()
        for index, line in enumerate(sys.stdin.readlines())
        if index in indexes
    ]

    word_list = split_to_words(sublines)

    # dict counter
    counts = dict()
    for w in word_list:
        counts[w] = counts.get(w, 0) + 1

  	# sort by desc value then asc key
    sorted_count = sorted(counts.items(), key=lambda x: (-x[1], x[0]))[0:19]

  	# first element to list ret
    ret = [word[0] for word in sorted_count] 

    for word in ret:
        print(word)

process(sys.argv[1])
