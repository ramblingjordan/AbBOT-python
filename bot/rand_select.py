#!/usr/bin/env python3
import random

def random_select_weighted_list(ls):
    return random.choices([k[1] for k in ls], weights = [k[0] for k in ls], k = 1)[0]
