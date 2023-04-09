def print_rangoli(size):
    # your code goes here
    g = size + (size-1)
    for i in range(size, 0, -1):
        for s in range(1,g):
            print("-", end="")
        for c in reversed(range(i, size+1)):
#            p = (c+97-1)
#            if(c>i):
#                print((chr)(p), end="-")
#            else:
#                print((chr)(p), end ="")
#            #p = p-1
#        if i<size:
#            q = i + 97
#            for a in reversed(range(i-1, size-1)):
#
#                print(f"-{(chr)(q)}", end ="")
#                q = q + 1
#        for t in range(1,g):
#            print("-", end="")
#        print()
#        g=g-2

print_rangoli(5)