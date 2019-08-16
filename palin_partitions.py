'''
Given a string, a partitioning of the string is a palindrome partitioning if
every substring of the partition is a palindrome. For example,
“aba|b|bbabb|a|b|aba” is a palindrome partitioning of “ababbbabbababa”.
Determine the fewest cuts needed for palindrome partitioning of a given string.
For example, minimum 3 cuts are needed for “ababbbabbababa”. The three cuts are
“a|babbbab|b|ababa”. If a string is palindrome, then minimum 0 cuts are needed.
If a string of length n containing all different characters, then minimum n-1
cuts are needed.
'''

def num_palin_parts(s, mem={}):
    if s in mem:
        return mem[s]
    
    if s == s[::-1]:
        return 0

    min_cuts = 10**10
    for i in range(1, len(s)+1):
        sub = s[:i]
        print(sub)
        if sub[::-1] != sub:
            continue

        num_cuts = palin_parts(s[i:])+1
        min_cuts = min(num_cuts, min_cuts)
        

    mem[s] = min_cuts
    return min_cuts


def palin_parts(s, mem = {}):
    if s in mem:
        return mem[s]
    
    if s == s[::-1]:
        return [s]

    palins = [0]*len(s)
    for i in range(1, len(s)+1):
        sub = s[:i]
        if sub[::-1] != sub:
            continue

        sub_palins = palin_parts(s[i:])
        if len(sub_palins)+1 < len(palins):
            palins = [sub] + sub_palins
        

    mem[s] = palins
    return palins


ss = 'ababbbabbbbbbbbbbbbaaaaabbbbbbbbbbbbbbbbbabbbabababbbababababababaaaaaabbbababababbbaaabbbaaaabbababa'
print(palin_parts(ss))

