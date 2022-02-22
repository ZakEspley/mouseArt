import numpy as np
import time
from itertools import groupby, zip_longest
from numba import jit

filename = "data/lotsOfRisk.log"

rawData = np.genfromtxt(filename, delimiter=",")

delta = np.delete(rawData, [0,1,2,5,6], axis=1)
print(f"Delta Data Length: {len(delta)}")




# @jit(nopython=True, parallel=True)
def filterFast(delta):
    lastdx = lastdy = 0
    filteredDelta1 = np.empty((0,2))
    for dx, dy in delta:
        if lastdx - dx == 0 and lastdy - dy == 0:
            continue
        lastdx = dx
        lastdy = dy
        filteredDelta1 = np.append(filteredDelta1, np.array([[dx, dy]]), axis=0)
    return filteredDelta1
t1 = time.perf_counter_ns()
filteredDelta1 = filterFast(delta)
t2 = time.perf_counter_ns()
print(f'Filtered Data Length: {len(filteredDelta1)}')
print(f'Filtering Took {(t2-t1)*1E-9} s')

# f = np.array([i for i,j in zip_longest(delta, delta[1:], fillvalue=[-1,-1]) if all([i[0]==j[0],
#  i[1]==j[1]])])
t1 = time.perf_counter_ns()
f = np.array([np.array(k)*len(list(g)) for k,g in groupby(delta, key=lambda t: (t[0], t[1]))])
t2 = time.perf_counter_ns()
print(f"Second Filter took {(t2-t1)*1E-9} s")
print(f"Length: {len(f)}")

t1 = time.perf_counter_ns()
position = np.cumsum(delta, axis=0)
fp = np.array([i for i,j in groupby(position, key=lambda t: (t[0], t[1]))])
t2 = time.perf_counter_ns()
print(f"Position took {(t2-t1)*1E-9} s")
print(f"Length of position {len(position)}, length after filter {len(fp)}")

# print(delta)
# print(filteredDelta1)
