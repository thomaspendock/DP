'''
Given a rope of length n meters, cut the rope in different parts of integer
lengths in a way that maximizes product of lengths of all parts. You must make
at least one cut. Assume that the length of rope is more than 2 meters.
'''

calls = 0
mems = 0


def gpp_fast(n):
    rem_1 = n%3 == 1
    return 3**(n//3 - rem_1) * max(1, n%3 + 3*rem_1)

def gpp(n, mem=[1, 1, 1]):
    global calls, mems

    calls += 1
    
    # Initialize call storage
    if len(mem) == 3 and n > 2:
        mem += [0]*(n-2)

    # Return stored call if possible
    if mem[n]:
        mems += 1
        return mem[n]
    
    largest = 0
    for rem_length in range(1, n+1):
        product = rem_length * gpp(n-rem_length)
        largest = max(largest, product)

    return largest

x = 21
print(gpp(x), gpp_fast(x))
print(calls, mems)
        
        
    
