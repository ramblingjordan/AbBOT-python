#!/usr/bin/env python3
import random
from rand_select import random_select_weighted_list
import seaborn as sns
import matplotlib.pyplot as plt

def gen_typo_odds():
    return 1.0 - (random.betavariate(5, 1.5) * 0.3 + 0.6995)

def add_typos(in_str):
    typo_odds = gen_typo_odds()
    sub_dict = {
        'a': [
            # First element is always 1 - typo_odds and it's always the correct
            # letter. The rest of the elements are incorrect substitutions.
            # They can also be multiple letters or zero letters.
            (1 - typo_odds, 'a'),
            # Make sure that these add up to 1.0.
            (0.1 * typo_odds, 's'),
            (0.2 * typo_odds, 'q'),
            (0.1 * typo_odds, 'w'),
            (0.5 * typo_odds, 'e'),
            (0.1 * typo_odds, 'i')
        ],
    }
    out_str = ''
    for k in in_str:
        if k in sub_dict:
            out_str += random_select_weighted_list(sub_dict[k])
        else:
            out_str += k
    return out_str

if __name__ == "__main__":
    output = [ gen_typo_odds() for k in range(1000000) ]
    sns.kdeplot(output)
    plt.show()
