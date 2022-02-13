"""Generate Markov text from text files."""

import sys
# print()
# print(sys.argv)

from random import choice

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    file = open(file_path)
    contents = file.read()
    file.close()  

    # file = with open(file_path).read()

    return contents #'Contents of your file as one long string'
# print(open_and_read_file("green-eggs.txt"))
# contents = open_and_read_file(file_path)
# break()  #stops till here. won't run the following. 

def make_chains(contents):
    """Take input text as string; return dictionary of Markov chains.
 
    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    words = contents.split() #words is a list of words

    # for i in range(len(words) - 1):
    #     key = (words[i], words[i + 1])
    #     if words[i+1] == words[-1]:
    #         break
    #     else:
    #         value = (words[i + 2])        
    #     if key not in chains.keys():
    #         chains[key] = [value]
    #         # chains[key].append(value)
    #     else:
    #         chains[key].append(value)
        
    i = 0
    for i in range(len(words) - 2):
        key = (words[i], words[i+1]) #creating tuple

        if key in chains:
            #append value of words at i+2, append to the dictionary at teh value of key
            chains[key].append(words[i+2])
        else:
            #making a new list as the value
            value = [words[i+2]]
            #make th evalue of words at i+2
            chains[key] = value

    return chains

# chains=make_chains(contents)


# def make_text(chains): 
#     """Return text from chains."""
#     words= []

#     key = choice(list(chains.keys())) # key is a tuple
#     chosen_word = choice(chains[key]) # chosen_word is a string

#     words.extend(list(key))
#     words.append(chosen_word)

#     new_key = (key[1], chosen_word)

#     while new_key in chains.keys():
#         chosen_word = choice(chains[new_key])
#         words.append(chosen_word)
#         new_key = (new_key[1], chosen_word)

#     return ' '.join(words)

def make_text(chains):
    """Return text from chains."""

    words = []
    #pick a key (word1, word2)
    keys = chains.keys() # returns list of tuples as dict_keys datatype, which is not subscriptable
    keys_list = list(keys) #transtype to proper subscriptable list
    word_pair = choice(keys_list) #randomly pick a tuple from list
    words.append(word_pair[0]) #append first word of tuple to words list
    
    while True:
        # if word_pair == ('Sam', 'I'):
        #     words.append(('Sam', 'I')[1])
        #     words.append('I')
            
        words.append(word_pair[1])
        
        if word_pair in chains:
            #pick a random word from the list of words associated with key word pair (word3)    
            next_word = choice(chains[word_pair])
            word_pair = (word_pair[1], next_word) #create next word-pair from second word of previous key-pair and the next word
            #last word of first key-pair and the word we just picked for 'next-word' and make the next tuple (word2, word3)
    
        else:
            break

    # While True: repeat, and build words list. Once a word-pair is created that is not present in original chains
    # true loop will break, and we will join all words in words list to form a string sentence

    return ' '.join(words) #create string from words list

# print(make_text(chains))

#############################
# using sys.argv to process a file. Pass in this file from the command line, using sys.argv.
# file_path = sys.argv[1] # a string
    # contents = open_and_read_file(file_path)

    # # Get a Markov chain
    # chains = make_chains(contents)

    # # Produce random text
    # random_text = make_text(chains)

    # print(random_text)
#####################################

# using sys.argv to process multiple files, one by one. Pass in files from the command line, using sys.argv.
for file_path in sys.argv[1:]:

    # Open the file and turn it into one long string
    contents = open_and_read_file(file_path)

    # Get a Markov chain
    chains = make_chains(contents)

    # Produce random text
    random_text = make_text(chains)

    print(random_text)



