from itertools import product
A = list(map(int,input().split()))
B = list(map(int,input().split()))

[print(i,end=' ') for i in product(A,B) ]