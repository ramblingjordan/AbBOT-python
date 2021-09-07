#!/usr/bin/env python3
import random
from collections import Counter
from typos import add_typos

def random_select_weighted_list(ls):
    return random.choices([k[1] for k in ls], weights = [k[0] for k in ls], k = 1)[0]

suspect_words = [
  (1.0, 'suspect'),
  (0.3, 'have reason to suspect'),
  (1.0, 'believe'),
  (0.3, 'have reason to believe'),
  (1.0, 'think'),
  (0.5, 'have evidence'),
  (0.2, 'have strong evidence'),
  (1.0, 'am convinced'),
  (1.0, 'am certain'),
  (1.0, 'can prove'),
  (1.0, 'have proof'),
]
my_family_words = [
  (0.5, 'father'),
  (0.5, 'mother'),
  (1.0, 'brother'),
  (1.0, 'sister'),
  (0.5, 'older brother'),
  (0.5, 'older sister'),
  (0.5, 'younger brother'),
  (0.5, 'younger sister'),
  (1.0, 'cousin'),
  (2.0, 'aunt'),
  (0.5, 'uncle'),
  (0.6, 'daughter'),
  (0.6, 'son'),
  (0.2, 'step-son'),
  (0.1, 'step son'),
  (0.2, 'step-daughter'),
  (0.1, 'step daughter'),
  (0.7, 'nephew'),
  (0.7, 'niece'),
  (0.5, 'grandmother'),
  (0.2, 'grandma'),
  (0.5, 'grandfather'),
  (0.2, 'grandpa'),
  (0.5, 'granddad'),
  (1.0, 'grandson'),
  (1.0, 'granddaughter'),
  (1.0, 'son-in-law'),
  (1.0, 'daughter-in-law'),
  (1.0, 'mother-in-law'),
  (1.0, 'father-in-law'),
  (0.1, 'half-brother'),
  (0.1, 'half-sister'),
]
subjects = [
  'science',
  'math',
  'history',
  'social studies',
  'chemistry',
  'algebra',
  'Spanish',
  'calculus',
  'art',
  'music',
  'gym',
  'English',
  'language arts',
  'composition',
  'geometry',
  'statistics',
  'physics',
  'earth science',
  'economics',
  'geography',
  'government',
  'French',
  'business',
]
my_teacher_words = [
  (1.0, 'teacher'),
  *[(0.2, k + ' teacher') for k in subjects],
  (0.5, 'tutor'),
  *[(0.1, k + ' tutor') for k in subjects],
  (1.0, 'babysitter'),
  (1.0, 'instructor'),
  *[(0.2, k + ' instructor') for k in subjects],
  (0.5, 'professor'),
  *[(0.1, k + ' professor') for k in subjects],
]
my_nonfamily_words = [
  (2.0, 'neighbor'),
  (0.6, 'next-door neighbor'),
  (1.5, 'boss'),
  (0.7, 'landlord'),
  (1.5, 'doctor'),
  (0.7, 'employee'),
  (0.5, 'roommate'),
  (1.0, 'friend'),
  (1.0, 'girlfriend'),
  (1.0, 'boyfriend'),
  (0.3, 'maid'),
  (0.2, 'live-in maid'),
  (0.1, 'live in maid'),
  (0.2, 'housekeeper'),
  (0.1, 'cleaning lady'),
  (2.0, 'ex'),
  (0.3, 'therapist'),
  (0.5, 'supervisor'),
  (1.0, 'employer'),
  (0.2, 'lawyer'),
  (0.4, 'dentist'),
  (0.2, 'plumber'),
  (1.5, 'pastor'),
  (0.5, 'deacon'),
  (0.8, 'priest'),
  (0.2, 'accountant'),
]
my_family_possessive_adj = [(k[0], k[1] + "'s ") for k in my_nonfamily_words]
my_family_possessive_adj.append((20.0, ''))
my_nonfamily_possessive_adj = [(k[0], k[1] + "'s ") for k in my_family_words]
my_nonfamily_possessive_adj.append((20.0, ''))
my_teacher_possessive_adj = [
  (0.2, 'younger brother'),
  (0.1, 'older brother'),
  (0.2, 'younger sister'),
  (0.1, 'older sister'),
  (0.8, 'brother'),
  (0.4, 'step-brother'),
  (0.8, 'sister'),
  (0.4, 'step-sister'),
  (1.0, 'cousin'),
  (2.0, 'daughter'),
  (2.0, 'son'),
  (0.4, 'step-son'),
  (0.2, 'step son'),
  (0.4, 'step-daughter'),
  (0.2, 'step daughter'),
  (0.7, 'nephew'),
  (0.7, 'niece'),
]
my_teacher_possessive_adj = [ (k[0], k[1] + "'s ") for k in my_teacher_possessive_adj ]
violated_words = [
  (8.0, 'violated'),
  (8.0, 'disregarded'),
  (8.0, 'disobeyed'),
  (4.0, 'assisted someone in violating'),
  (4.0, 'assisted someone in breaking'),
  (4.0, 'assisted someone in disobeying'),
  (3.0, 'helped someone violate'),
  (3.0, 'helped someone disobey'),
  (3.0, 'helped someone break'),
  (3.0, 'helped violate'),
  (3.0, 'helped break'),
  (3.0, 'helped disobey'),

  (0.4, 'helped someone have an abortion, violating'),
  (0.4, 'helped someone have an abortion, breaking'),
  (0.4, 'helped someone have an abortion in violation of'),

  (0.4, 'helped someone get an abortion, violating'),
  (0.4, 'helped someone get an abortion, breaking'),
  (0.4, 'helped someone get an abortion in violation of'),

  (0.4, 'helped someone to get an abortion, violating'),
  (0.4, 'helped someone to get an abortion, breaking'),
  (0.4, 'helped someone to get an abortion in violation of'),

  (0.1, 'helped someone kill her child and violate'),
  (0.1, 'helped someone kill her baby and violate'),
  (0.1, 'helped someone kill a child and violate'),
  (0.1, 'helped someone kill a baby and violate'),

  (0.1, 'helped someone kill a child and disobey'),
  (0.1, 'helped someone kill a baby and disobey'),
  (0.1, 'helped someone kill her child and disobey'),
  (0.1, 'helped someone kill her baby and disobey'),

  (0.4, 'helped someone abort her child and violate'),
  (0.4, 'helped someone abort her baby and violate'),
  (0.4, 'helped someone abort her child and disobey'),
  (0.4, 'helped someone abort her baby and disobey'),

  (0.1, 'helped someone murder her child and violate'),
  (0.1, 'helped someone murder her baby and violate'),

  (0.1, 'helped someone murder a child and disobey'),
  (0.1, 'helped someone murder a baby and disobey'),
  (0.1, 'helped someone murder her child and disobey'),
  (0.1, 'helped someone murder her baby and disobey'),

  (0.1, 'helped someone murder her child in violation of'),
  (0.1, 'helped someone murder her baby in violation of'),
  (0.1, 'helped someone murder a child in violation of'),
  (0.1, 'helped someone murder a baby in violation of'),

  (0.1, 'helped someone kill her child in violation of'),
  (0.1, 'helped someone kill her baby in violation of'),
  (0.1, 'helped someone kill a child in violation of'),
  (0.1, 'helped someone kill a baby in violation of'),

  (0.1, 'helped someone kill her child, violating'),
  (0.1, 'helped someone kill her baby, violating'),
  (0.1, 'helped someone kill a child, violating'),
  (0.1, 'helped someone kill a baby, violating'),

  (0.1, 'helped someone murder a child, violating'),
  (0.1, 'helped someone murder a baby, violating'),
  (0.1, 'helped someone murder her child, violating'),
  (0.1, 'helped someone murder her baby, violating'),

  (0.1, 'aided in the killing of a child, violating'),
  (0.1, 'aided in the killing of a baby, violating'),
  (0.1, 'aided in the killing of her child, violating'),
  (0.1, 'aided in the killing of her baby, violating'),
  (0.1, 'aided her in killing her baby, violating'),
  (0.1, 'aided her in killing her child, violating'),

  (0.1, 'aided in the killing of a child, disobeying'),
  (0.1, 'aided in the killing of a baby, disobeying'),
  (0.1, 'aided her in killing her baby, disobeying'),
  (0.1, 'aided her in killing her child, disobeying'),

  (0.1, 'aided in the killing of a child, breaking'),
  (0.1, 'aided in the killing of a baby, breaking'),
  (0.1, 'aided in the killing of her child, breaking'),
  (0.1, 'aided in the killing of her baby, breaking'),
  (0.1, 'aided in the killing of a child, breaking'),
  (0.1, 'aided in the killing of a baby, breaking'),

  (0.1, 'aided her in killing her baby, breaking'),
  (0.1, 'aided her in killing her child, breaking'),
  (0.1, 'aided her in killing her baby, breaking'),
  (0.1, 'aided her in killing her child, breaking'),

  (0.1, 'aided in the killing of a child, in violation of'),
  (0.1, 'aided in the killing of a baby, in violation of'),
  (0.1, 'aided in the killing of her child, in violation of'),
  (0.1, 'aided in the killing of her baby, in violation of'),
  (0.1, 'aided in the killing of a child, in violation of'),
  (0.1, 'aided in the killing of a baby, in violation of'),

  (0.1, 'aided her in killing her baby, in violation of'),
  (0.1, 'aided her in killing her child, in violation of'),
  (0.1, 'aided her in killing her baby, in violation of'),
  (0.1, 'aided her in killing her child, in violation of'),

  (0.1, 'aided in the killing of a child and violated'),
  (0.1, 'aided in the killing of a baby and violated'),
  (0.1, 'aided in the killing of her child and violated'),
  (0.1, 'aided in the killing of her baby and violated'),

  (0.1, 'aided her in killing her baby and violated'),
  (0.1, 'aided her in killing her child and violated'),
]
days_of_the_week = [
  'Sunday',
  'Monday',
  'Tuesday',
  'Wednesday',
  'Thursday',
  'Friday',
  'Saturday',
]
got_words = [
  'got', 'had', 'helped someone get', 'assisted someone in getting', 'helped someone have'
]
past_time_frames = [
  'last week', 'last month', 'this week', 'this month', 'yesterday', 'a week ago', 'two weeks ago', 'two days ago', 'on the weekend',
  'this weekend', 'last weekend'
]
past_time_frames.extend([ 'last ' + k for k in days_of_the_week ])
past_time_frames.extend([ 'on ' + k for k in days_of_the_week ])
will_get_words = [
  'is getting', 'will get', 'plans on having', 'is trying to get', 'is trying to have', 'will try to get', 'is helping someone get', 'is planning to get', 'is planning on getting',
  'plans to get'
]
past_time_frames.extend(['last ' + k for k in days_of_the_week])
past_time_frames.extend(['on ' + k for k in days_of_the_week])
will_get_words = ['is getting', 'will get', 'plans on having', 'is trying to get', 'is trying to have', 'will try to get']
future_time_frames = [
  'next week', 'this week', 'tomorrow', 'two days from now', 'a week from now', 'after she leaves work', 'after work', 'on the weekend',
  'this weekend', 'next weekend'
]
future_time_frames.extend(['next ' + k for k in days_of_the_week])
future_time_frames.extend(['on ' + k for k in days_of_the_week])
abortion_ban_words = [
  'abortion ban', 'ban on abortion', 'law on abortion', 'recent abortion law', 'abortion restrictions', 'restrictions on abortion',
]
abortion_ban_words = [ *["recently passed " + k for k in abortion_ban_words], *[k for k in abortion_ban_words] ]
abortion_ban_words = [ *["Texas's " + k for k in abortion_ban_words], *["the " + k for k in abortion_ban_words] ]
abortion_ban_words.extend(['Texas law', 'the new law', 'Texas law on abortion', 'the Texas law on abortion', 'the Texas abortion law',
  'the new Texas abortion law', 'the recently passed Texas abortion law', 'new abortion law'])

def gen_abortion_prompt_I(accused):
  abortion_prompt = 'I '
  abortion_prompt += random_select_weighted_list(suspect_words)
  abortion_prompt += random.choices([' that', ''], weights=[0.75, 0.25], k=1)[0]
  abortion_prompt += ' my '
  abortion_prompt += accused
  abortion_prompt += random.choice([' has ', ' '])
  abortion_prompt += random_select_weighted_list(violated_words)
  abortion_prompt += ' '
  abortion_prompt += random.choice(abortion_ban_words)
  abortion_prompt += '.'
  return abortion_prompt

def gen_abortion_prompt_My(accused):
  abortion_prompt = 'My '
  abortion_prompt += accused
  abortion_prompt += ' '
  past = random.random() > 0.5
  if past:
    abortion_prompt += random.choice(got_words)
  else:
    abortion_prompt += random.choice(will_get_words)
  abortion_prompt += ' an'
  abortion_prompt += random.choices(['', ' illegal', ' unlawful'], weights=[0.625, 0.375 / 2.0, 0.375 / 2.0], k=1)[0]
  abortion_prompt += ' abortion'
  if random.random() > 0.5:
    abortion_prompt += ' '
    if past:
      abortion_prompt += random.choice(past_time_frames)
    else:
      abortion_prompt += random.choice(future_time_frames)
  abortion_prompt += '.'
  return abortion_prompt

counter = 0

def gen_abortion_prompt():
  global counter
  accused_family_person = random_select_weighted_list(my_family_possessive_adj)
  accused_family_person += random_select_weighted_list(my_family_words)
  accused_nonfamily_person = random_select_weighted_list(my_nonfamily_possessive_adj)
  accused_nonfamily_person += random_select_weighted_list(my_nonfamily_words)
  accused_teacher = random_select_weighted_list(my_teacher_possessive_adj)
  accused_teacher += random_select_weighted_list(my_teacher_words)
  accused = random_select_weighted_list([
    (1.0, accused_family_person),
    (1.5, accused_nonfamily_person),
    (0.5, accused_teacher)
  ])
  abortion_prompts = [
    (1.0, gen_abortion_prompt_I(accused)),
    (1.0, gen_abortion_prompt_My(accused))
  ]
  counter += 1
  if random.random() < 0.001:
    print('\r\x1b[K' + str(counter), end='')
  return random_select_weighted_list(abortion_prompts)
  #return add_typos(random_select_weighted_list(abortion_prompts))

bigram_counter = Counter()
trigram_counter = Counter()
quadgram_counter = Counter()

def check_ngram_frequency(prompt):
  words = prompt.split()
  for i in range(len(words) - 1):
    cur_bigram = ' '.join(words[i:i+2])
    bigram_counter[cur_bigram] += 1
  for i in range(len(words) - 2):
    cur_trigram = ' '.join(words[i:i+3])
    trigram_counter[cur_trigram] += 1
  for i in range(len(words) - 3):
    cur_quadgram = ' '.join(words[i:i+4])
    quadgram_counter[cur_quadgram] += 1
  return prompt

def write_ngram_to_file(counter, filename, total):
    with open(filename, 'w') as writer:
        for k, v in counter.most_common():
            writer.write( "{} {}\n".format(k, float(v) / total) )
            if float(v) / total < 0.001:
                break

if __name__ == "__main__":
  total_number = 2000000
  sample_abortion_prompts = [ check_ngram_frequency(gen_abortion_prompt()) for k in range(total_number) ]
  for k in sorted(list(sample_abortion_prompts)[:200], key = lambda o: random.random()):
    print(k)
  unique = len(set(sample_abortion_prompts))
  print('Duplicates: ' + str(total_number - unique))
  print('Unique:     ' + str(unique))
  write_ngram_to_file(bigram_counter, 'bigram_freq.txt', len(sample_abortion_prompts))
  write_ngram_to_file(trigram_counter, 'trigram_freq.txt', len(sample_abortion_prompts))
  write_ngram_to_file(quadgram_counter, 'quadgram_freq.txt', len(sample_abortion_prompts))
