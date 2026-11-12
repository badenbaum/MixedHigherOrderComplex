###### higher_order_complex.py #######

## sage: wrap([m,n_1,n_2,...,n_k,p],r )
from sage.all import *

def wrap(N,r):
    D = higher_order_complex(N,r)
    print("D is pure == " + str(D.is_pure()))
    print("dimension == " + str(D.dimension()))
    print("h-vector == " + str( D.h_vector() ))
    return D



### Higher order complex for a product of chains

### [m] x [n_1] x [n_2] x ... x [n_k] x [p]

### N = [m,n_1, n_2, ..., n_k, p]

def higher_order_complex(N,l):
    r = l+1
    groundset = list(cartesian_product([list(range(n)) for n in N]))
    
    CT = []
    for t in range(1,len(N)):
        CT += crossing_tuples(groundset, r, t)

    G = list(Set(flatten(CT)))
    Delta = SimplicialComplex([G])

    Delta.remove_faces(CT)
    return Delta




def crossing_tuples(G, r, t):
    T = Subsets(G,r)
    T = [sorted(M) for M in T]

    ret = []
    for M in T:
        antichain = True
        for j in range(r):
            for i in range(j):
                if not is_cross(M[i],M[j], t):
                    antichain = False
        if antichain:
            ret += [M]

    return ret
        

def is_cross(A,B,t):

    l = len(A)

    D = [A[i] - B[i] for i in range(l)]
    
    if all( [D[i] == 0 for i in range(t)] ):
        return False
    if all( [D[i] == 0 for i in range(t,l)] ):
        return False

    left = max([ i for i in range(t) if D[i] != 0 ])
    right = min([ i for i in range(t,l) if D[i] != 0] )

    return D[left] * D[right] < 0


