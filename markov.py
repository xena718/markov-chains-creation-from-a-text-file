"""Generate Markov text from text files."""

from random import choice

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    file = open(file_path)
    contents = file.read()
    file.close()  

    return contents #'Contents of your file as one long string'
# print(open_and_read_file("green-eggs.txt"))
# contents = open_and_read_file(file_path)
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

    for i in range(len(words) - 1):
        key = (words[i], words[i + 1])
        if words[i+1] == words[-1]:
            break
        else:
            value = (words[i + 2])        
        if key not in chains.keys():
            chains[key] = []
            chains[key].append(value)
        else:
            chains[key].append(value)
        

         # list = [1,2,3,4]

    return chains

# chains=make_chains(contents)


def make_text(chains):
    """Return text from chains."""
    words= []

    key = choice(list(chains.keys())) # key is a tuple
    chosen_word = choice(chains[key]) # chosen_word is a string
    # link = key+chosen_word
    words.append(key[0])
    words.append(key[1])
    words.append(chosen_word)

    new_key = (key[1], chosen_word)

    while new_key in chains.keys():
        chosen_word = choice(chains[new_key])
        words.append(chosen_word)
        new_key = (new_key[1], chosen_word)

    return ' '.join(words)

# print(make_text(chains))

file_path = 'green-eggs.txt'

# Open the file and turn it into one long string
contents = open_and_read_file(file_path)

# Get a Markov chain
chains = make_chains(contents)

# Produce random text
random_text = make_text(chains)

print(random_text)
