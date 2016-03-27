from nltk.corpus import cmudict
from curses.ascii import isdigit

# load CMU pronunciation dictionary
prondict = cmudict.dict()

# count the number of syllables
numsyllables_pronlist = lambda l: len(filter(lambda s: isdigit(s.encode('ascii', 'ignore').lower()[-1]), l))
def numsyllables(word):
    try:
        return list(set(map(numsyllables_pronlist, prondict[word.lower()])))
    except KeyError:
        return [0]