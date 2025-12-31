import itertools
from .word_list import dict_words


def filter_words(word):
    all_words = []
    num_range = [i for i in range(2, len(word))]

    for num in num_range:
        comb_words = itertools.permutations(word, num+1)
        list_comb = [''.join(i) for i in comb_words]
        for i in list_comb:
            all_words.append(i)

    cookie_words = list(set([i for i in all_words if i in dict_words]))
    return cookie_words