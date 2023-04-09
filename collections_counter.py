from collections import Counter

# input list
n = int(input())
arr = list(map(int, input().split()))

# input set
m = int(input())
s = set(map(int, input().split()))

# using Counter to count the frequency of elements in arr
c = Counter(arr)

# iterating through the set s and finding the sum of frequencies
result = 0
for elem in s:
    if elem in c:
        result += c[elem]

# printing the result
print(result)