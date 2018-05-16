# COLLATZ CONJECTURE

import pandas as pd
import matplotlib.pyplot as plt

def collatz(n):
    '''For any number n, return the pathway it takes to get to 1.'''
    pathway = []
    m = n
    while m != 1:
        pathway.append(m)
        if m % 2 == 0:
            m = m // 2
        else:
            m = m * 3 + 1
    return pathway

def path_lengths(n):
    '''Return the length of each path from 2 to n.'''
    path_lengths = {}
    for i in range(2, n + 1):
        path_length = len(collatz(i))
        path_lengths[i] = path_length
    return path_lengths

def step_in_path_count(n):
    '''Count how many paths each step was a part of. Counts all all_paths
    from 2 to n.'''
    all_paths = []
    step_touch_count = {}
    for i in range(2, n + 1):
        path = collatz(i)
        all_paths.append(path)

    for path in all_paths:
        for step in path:
            if step in step_touch_count:
                step_touch_count[step] += 1
            else:
                step_touch_count[step] = 1
    return step_touch_count

step_touches = step_in_path_count(10)
path_lengths = path_lengths(100)

s = pd.Series(path_lengths, name = 'Path Lengths')
s.index.name = 'Start'
s.reset_index()
s.plot()
plt.show()
