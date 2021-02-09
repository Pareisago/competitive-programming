# A Python program to print all  
# permutations using library function 
from itertools import permutations

myset = set()
# Get all permutations of [1, 2, 3] 
for p in permutations('XXYY'):
  myset.add(p)

print(myset)