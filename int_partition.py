#p(n,m)=p(n-m,m)+p(n,m-1)
'''



def accel_asc(n):
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]
       
for i in accel_asc(6): print(i)
'''

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

