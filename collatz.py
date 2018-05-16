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

def steps(n):
    steps = len(collatz(n))
    return steps

all_paths = []
step_touch_count = {}
for i in range(2, 101):
    path = collatz(i)
    all_paths.append(path)

for path in all_paths:
    for step in path:
        if step in step_touch_count:
            step_touch_count[step] += 1
        else:
            step_touch_count[step] = 1

s = pd.Series(step_touch_count, name = 'Step Touches')
s.index.name = 'Step'
s.reset_index()
s.plot(xlim = (0,100))
plt.show()
