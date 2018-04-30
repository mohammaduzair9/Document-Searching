#importing basic libraries
import re
import math 
import numpy as np

#making the dictionary of the document
def make_dictionary(document):
    dictionary = {}
    with open(document, 'r') as file:
        # .lower() returns a version with all upper case characters replaced with lower case characters.
        text = file.read().lower()
        # replaces anything that is not a lowercase letter, a space, or an apostrophe with a space:
        text = re.sub('[^a-z\ \']+', " ", text)  # For some reason, even though the text is in lower case, the code does't work unless i redo that condition
        Words = list(text.split())  # put text into an empty list using split()
        for i in Words:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
    return dictionary

# making the inverted index of the document
def make_invertedIndex(document):
    inverted = {}
    with open(document, 'r') as f:
        lines = f.read().splitlines()   # making a list of all documents seperated by a newline character

    idx = 1                                         # maintaining the current document index
    for docs in lines:
        doc_words = list(docs.split())               # getting the words od each document in a list
        # for each word in documents
        for word in doc_words:
            if word in inverted:                    # if the word exists in the inverted index
                if idx not in inverted[word]:       # if current document is not in the value of this word
                    inverted[word].append(idx)      # add the current document as a value for the current word
            else:
                inverted[word] = [idx]              # if word is not a key of invertedindex then make a new key
        idx += 1;
    return inverted

with open('docs.txt', 'r') as f:
    lines = f.read().splitlines()

# making the dictionary
dictionary = make_dictionary('docs.txt')
print "Words in dictionary:  " , len(dictionary)

# making the inverted index
inverted = make_invertedIndex('docs.txt')

