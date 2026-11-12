
#### detideal.py #####

# sage: R,I = make_ideal([m,n_1,n_2,...,n_k,p], r)
# sage: I.hilbert_series().numerator()
from sage.all import *


def make_ideal(N,r):
    gs = list(cartesian_product([list(range(n)) for n in N]))    

    R = PolynomialRing(QQ, ['x' + tuptoid(a) for a in gs])

    M = []
    for t in range(1, len(N)):
        A = build_array(N, R, t)
        M += A.minors(r+1)

    I = R.ideal(M)

    return R,I


def build_array(N, R, t):
    rowlen = N[:t]
    collen = N[t:]
    rowlen.reverse()
    
    rows = list(cartesian_product([list(range(n)) for n in rowlen]))
    cols = list(cartesian_product([list(range(n)) for n in collen]))

    rows = [tuple(reversed(A)) for A in rows]

    return matrix([ [tuptovar(tuple(list(a)+list(b)),R) for b in cols] for a in rows])



def tuptoid(a):
    return ''.join(map(str,a))

def vartotup(v):
    s = str(v)
    return (int(s[1]),int(s[2]),int(s[3]))

def tuptovar(a,R):
    return R('x' + tuptoid(a))



