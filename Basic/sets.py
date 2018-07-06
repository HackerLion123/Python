

""" ways of declaring sets """

A = {1,2,6,7,8}
B = set([5,4,9,1,12,35]) 
C = set() # Empty set # C = {} is a empty dict

print(dir(C))

print(A.issubset(B))

print(A.isdisjoint(B))

print(A.union(B))