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

with open('docs.txt', 'r') as f:
    lines = f.read().splitlines()

# making the dictionary
dictionary = make_dictionary('docs.txt')
print "Words in dictionary:  " , len(dictionary)

