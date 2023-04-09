from itertools import permutations
s, k = input().split()
l = list(permutations(s,int(k)))
l.sort()
for i in l:
    print(''.join(list(i)),end='\n')

