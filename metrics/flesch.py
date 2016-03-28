import numpy as np
from nltk.tokenize import sent_tokenize, word_tokenize
from metrics.syllables import numsyllables

not_punctuation = lambda w: not (len(w)==1 and (not w.isalpha()))
get_word_count = lambda text: len(filter(not_punctuation, word_tokenize(text)))
get_sent_count = lambda text: len(sent_tokenize(text))

def text_statistics(text):
    word_count = get_word_count(text)
    sent_count = get_sent_count(text)
    syllable_count = sum(map(lambda w: max(numsyllables(w)), word_tokenize(text)))
    return word_count, sent_count, syllable_count

# Flesch reading ease
# reference: https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests
flesch_formula = lambda word_count, sent_count, syllable_count : 206.835 - 1.015*word_count/sent_count - 84.6*syllable_count/word_count
def flesch(text):
    word_count, sent_count, syllable_count = text_statistics(text)
    return flesch_formula(word_count, sent_count, syllable_count)

# Flesch-Kincaid grade level
# reference: https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests
fk_formula = lambda word_count, sent_count, syllable_count : 0.39 * word_count / sent_count + 11.8 * syllable_count / word_count - 15.59
def flesch_kincaid(text):
    word_count, sent_count, syllable_count = text_statistics(text)
    return fk_formula(word_count, sent_count, syllable_count)
