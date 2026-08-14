#!/usr/bin/env python
"""
Reducer takes words with their class and partial counts and computes totals.
INPUT:
    word \t class \t partialCount 
OUTPUT:
    word \t class \t totalCount  
"""
import re
import sys

# initialize trackers
current_word = None
spam_count, ham_count = 0,0

# read from standard input
for line in sys.stdin:
    # parse input
    word, is_spam, count = line.split('\t')
    
############ YOUR CODE HERE #########
    # tally counts from the current key
    is_spam, count = int(is_spam), int(count)
    if current_word == word:
        if is_spam == 1:
            spam_count += count
        else:
            ham_count += count
    # emit current total and start a new tally 
    else: 
        if current_word:
            print(f'{current_word}\t1\t{spam_count}')
            print(f'{current_word}\t0\t{ham_count}')
            
        current_word = word
        
        if is_spam == 1:
            spam_count = count
            ham_count = 0
        else:
            ham_count = count
            spam_count = 0

# last record
if current_word is not None:
    if is_spam == 1:
        print(f'{current_word}\t1\t{spam_count}')
    else:
        print(f'{current_word}\t0\t{ham_count}')





############ (END) YOUR CODE #########