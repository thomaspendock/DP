
def partition(x):

    mem = {}
    
    def p(n,m):
        if m > n: return 0
        if m < 2: return m
        
        if (n,m) in mem:
            return mem[(n,m)]
        else:
            ans = p(n - m, m) + p(n - 1, m - 1)
            mem[(n,m)] = ans
            return ans

    total = 0
    for i in range(0, x+1):
        total += p(x, x-i)
    return total

print(partition(20))

