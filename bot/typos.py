#!/usr/bin/env python3
import random
import re

def random_select_weighted_list(ls):
    return random.choices([k[1] for k in ls], weights = [k[0] for k in ls], k = 1)[0]

def gen_typo_odds():
    return 1.0 - (random.betavariate(0.5, 0.15) * 0.3 + 0.699995)

def add_typos(in_str):
    typo_odds = gen_typo_odds()
    # Outside of English transliterations, the letter 'q' is always followed by
    # a 'u'. By combining them into one letter, typos are easier to introduce.
    in_str = re.sub('qu', 'q', in_str)
    in_str = re.sub("'s", "'", in_str)
    sub_dict = {
        'a': [
            # First element is always 1 - typo_odds and it's always the correct
            # letter. The rest of the elements are incorrect substitutions.
            # They can also be multiple letters or zero letters.
            (1 - typo_odds, 'a'),
            # Make sure that these add up to 1.0.
            (0.2 * typo_odds, 'e'),
            (0.1 * typo_odds, 'i')
        ],
        'b': [
            (1 - typo_odds, 'b'),
            (0.2 * typo_odds, 'p'),
            (0.1 * typo_odds, 'h'),
            (0.1 * typo_odds, 'n'),
        ],
        'c': [
            (1 - typo_odds, 'c'),
            (0.1 * typo_odds, 'ts'),
            (0.3 * typo_odds, 's'),
            (0.3 * typo_odds, 'k'),
        ],
        'd': [
            (1 - typo_odds, 'd'),
            (0.5 * typo_odds, 't'),
        ],
        'e': [
            (1 - typo_odds, 'e'),
            (0.1 * typo_odds, 'a'),
            (0.5 * typo_odds, 'i'),
        ],
        'f': [
            (1 - typo_odds, 'f'),
            (0.5 * typo_odds, 'v'),
        ],
        'g': [
            (1 - typo_odds, 'g'),
            (0.1 * typo_odds, 'k'),
        ],
        'h': [
            (1 - typo_odds, 'h'),
            (0.2 * typo_odds, ''),
        ],
        'i': [
            (1 - typo_odds, 'i'),
            (0.3 * typo_odds, 'e'),
            (0.1 * typo_odds, 'a'),
            (0.01 * typo_odds, 'k'),
        ],
        'j': [
            (1 - typo_odds, 'j'),
            (0.01 * typo_odds, 'ch'),
        ],
        'k': [
            (1 - typo_odds, 'k'),
            (0.1 * typo_odds, 'g'),
            (0.4 * typo_odds, 'c')
        ],
        'l': [
            (1 - typo_odds, 'l'),
            (0.03 * typo_odds, 'r'),
            (0.03 * typo_odds, 'w'),
        ],
        'm': [
            (1 - typo_odds, 'm'),
            (0.5 * typo_odds, 'n'),
        ],
        'n': [
            (1 - typo_odds, 'n'),
            (0.5 * typo_odds, 'n'),
            (0.2 * typo_odds, 'b')
        ],
        'o': [
            (1 - typo_odds, 'o'),
            (0.2 * typo_odds, 'u'),
            (0.1 * typo_odds, 'p')
        ],
        'p': [
            (1 - typo_odds, 'p'),
            (0.5 * typo_odds, 'b'),
            (0.2 * typo_odds, 'o'),
        ],
        'q': [
            (1 - typo_odds, 'qu'),
            (0.8 * typo_odds, 'kw'),
        ],
        'r': [
            (1 - typo_odds, 'r'),
            (0.3 * typo_odds, 'l'),
            (0.1 * typo_odds, 't')
        ],
        's': [
            (1 - typo_odds, 's'),
            (0.1 * typo_odds, 'sh'),
            (0.2 * typo_odds, 'c'),
            (0.2 * typo_odds, 'z')
        ],
        't': [
            (1 - typo_odds, 't'),
            (0.5 * typo_odds, 'd'),
            (0.3 * typo_odds, 'th'),
            (0.1 * typo_odds, 'r')
        ],
        'u': [
            (1 - typo_odds, 'u'),
            (0.01 * typo_odds, 'yu'),
            (0.2 * typo_odds, 'o'),
            (0.1 * typo_odds, ''),
        ],
        'v': [
            (1 - typo_odds, 'v'),
            (typo_odds, 'f')
        ],
        'w': [
            (1 - typo_odds, 'w'),
            (0.5 * typo_odds, ''),
        ],
        'x': [
            (1 - typo_odds, 'x'),
            (0.6 * typo_odds, 'ks'),
            (0.1 * typo_odds, 'z'),
        ],
        'y': [
            (1 - typo_odds, 'y'),
            (0.5 * typo_odds, 'u'),
            (0.2 * typo_odds, 'h'),
            (0.1 * typo_odds, 'j')
        ],
        'z': [
            (1 - typo_odds, 'z'),
            (0.9 * typo_odds, 's'),
            (0.05 * typo_odds, 'x')
        ],
        ',': [
            (1 - typo_odds ** 0.5, ','),
            (0.9 * typo_odds ** 0.5, ''),
            (0.1 * typo_odds ** 0.5, '.'),
        ],
        '.': [
            (1 - typo_odds ** 0.75, '.'),
            (0.3 * typo_odds ** 0.75, ''),
            (0.3 * typo_odds ** 0.75, ','),
        ],
        "'": [
            (1 - typo_odds ** 0.5, "'s"),
            (0.7 * typo_odds ** 0.5, "s"),
            (0.3 * typo_odds ** 0.5, "s'")
        ]
    }
    out_str = ''
    words = in_str.split()
    out_words = []
    misspelled_words = {}
    for word in words:
        prev_char_in = ''
        prev_char_out = ''
        out_word = ''
        if word in misspelled_words and random.random() < 0.5:
            out_words.append(misspelled_words[word])
            continue
        for k in word:
            if k in sub_dict:
                if k == prev_char_in:
                    out_word += prev_char_out
                else:
                    prev_char_out = random_select_weighted_list(sub_dict[k])
                    out_word += prev_char_out
            else:
                out_word += k
            prev_char_in = k
        if out_word != word:
            misspelled_words[word] = out_word
        out_words.append(out_word)
    return ' '.join(out_words)
