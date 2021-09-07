#!/usr/bin/env python3
import random
import re
#import seaborn as sb
#import matplotlib.pyplot as plt

def random_select_weighted_list(ls):
  return random.choices([k[1] for k in ls], weights = [k[0] for k in ls], k = 1)[0]

def gen_typo_odds():
  return 1.0 - (random.betavariate(0.5, 0.15) * 0.3 + 0.699995)

#typo_data = []
#space_data = []
#punct_data = []

def add_typos(in_str, typo_odds = -1, space_typo_odds = -1, lowercase_odds = -1, punct_typo_odds = -1):
  #global typo_data
  #global space_data
  #global punct_data
  if typo_odds < 0:
    if random.random() < 0.1:
      typo_odds = 0.0
    else:
      typo_odds = gen_typo_odds()
  #  typo_data.append(typo_odds)
  if space_typo_odds < 0:
    space_typo_odds = gen_typo_odds() / 2.0
  #  space_data.append(space_typo_odds)
  if lowercase_odds < 0:
    lowercase_odds = random.random()
  uppercase_odds = random.random()
  if punct_typo_odds < 0:
    punct_typo_odds = (gen_typo_odds() + typo_odds ** 0.5) / 2.0
  #  punct_data.append(punct_typo_odds)
  in_str = re.sub('ies ', '\u2605 ', in_str)
  in_str = re.sub('es ', '\u2604 ', in_str)
  in_str = re.sub('ie ', '\u2606 ', in_str)
  in_str = re.sub('ie', '\u2603', in_str)
  in_str = re.sub('ei', '\u2602', in_str)
  # Outside of English transliterations, the letter 'q' is always followed by
  # a 'u'. By combining them into one letter, typos are easier to introduce.
  in_str = re.sub('qu', '\u2601', in_str)
  in_str = re.sub("'s", "\u2600", in_str)
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
    '\u2601': [
      (1 - typo_odds, 'qu'),
      (0.9 * typo_odds, 'kw'),
      (0.1 * typo_odds, 'q'),
    ],
    'r': [
      (1 - typo_odds, 'r'),
      (0.3 * typo_odds, 'l'),
      (0.1 * typo_odds, 't')
    ],
    's': [
      (1 - typo_odds, 's'),
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
    "\u2602": [
      (1 - typo_odds, 'ei'),
      (1.0 * typo_odds, 'ie')
    ],
    "\u2603": [
      (1 - typo_odds, 'ie'),
      (1.0 * typo_odds, 'ei')
    ],
    "\u2604": [
      (1 - typo_odds, 'es'),
      (1.0 * typo_odds, 's')
    ],
    "\u2605": [
      (1 - typo_odds, 'ies'),
      (1.0 * typo_odds, 'ys')
    ],
    "\u2606": [
      (1 - typo_odds, 'ie'),
      (1.0 * typo_odds, 'y')
    ],
    ',': [
      (1 - punct_typo_odds, ','),
      (0.9 * punct_typo_odds, ''),
      (0.1 * punct_typo_odds, '.'),
    ],
    '.': [
      (1 - punct_typo_odds, '.'),
      (0.3 * punct_typo_odds, ''),
      (0.1 * punct_typo_odds, ' .'),
      (0.01 * punct_typo_odds, '>'),
      (0.3 * punct_typo_odds, ','),
    ],
    "\u2600": [
      (1 - punct_typo_odds, "'s"),
      (0.7 * punct_typo_odds, "s"),
      (0.1 * punct_typo_odds, "s'"),
      (0.2 * punct_typo_odds, "'")
    ],
    "'": [
      (1 - punct_typo_odds, "'"),
      (1.0 * punct_typo_odds, "")
    ]
  }
  space_subs = [
    (1 - space_typo_odds, ' '),
    (0.9 * space_typo_odds, ''),
    (0.1 * space_typo_odds, '  ')
  ]
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
        if k == prev_char_in and random.random() > typo_odds:
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
  intermediate_str = ' '.join(out_words)
  if lowercase_odds < 0.1:
    intermediate_str = intermediate_str.lower()
  elif uppercase_odds < 0.1:
    intermediate_str = intermediate_str.upper()
  out_str = ''
  for k in intermediate_str:
    if k == ' ':
      out_str += random_select_weighted_list(space_subs)
    else:
      out_str += k
  return out_str

#def test_plot():
#  global typo_data
#  global space_data
#  global punct_data
#  sb.kdeplot(typo_data, label="Typos")
#  sb.kdeplot(space_data, label="Spaces")
#  sb.kdeplot(punct_data, label="Punctuation")
#  plt.legend()
#  plt.show()
