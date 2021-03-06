#!/usr/bin/env python3
import random

def random_select_weighted_list(ls):
    return random.choices([k[1] for k in ls], weights = [k[0] for k in ls], k = 1)[0]

def gen_typo_odds():
    return 1.0 - (random.betavariate(16, 2) * 0.3 + 0.6995)

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
