from pyscout import timekeeper
import numpy as np


print('Running simple pyscout demo...')
N = 100

while True:
    with timekeeper('Load Values'):
        aa = np.random.randn((N, N))
        bb = np.random.randn((N, N))

    with timekeeper('Calc1'):
        cc = aa**10 * bb**10

    with timekeeper('Calc2'):
        dd = aa.dot(bb)



