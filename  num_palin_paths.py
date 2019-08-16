'''
Given a matrix containing lower alphabetical characters only, we need to count
number of palindromic paths in given matrix. A path is defined as a sequence of
cells starting from top-left cell and ending at bottom-right cell. We are
allowed to move to right and down only from current cell.
'''

mem = {}

def palin_paths(m, cur_str='', cur_pos = (0,0)):
    max_x = len(m[0]) - 1
    max_y = len(m) - 1
    
    if cur_pos == (max_x, max_y):
        return int(cur_str == cur_str[::-1])

    key = cur_str, cur_pos
    if key in mem:
        return mem[key]

    cur_x, cur_y = cur_pos
    dirs = []
    if cur_x < max_x: dirs += [(1, 0)]
    if cur_y < max_y: dirs += [(0, 1)]

    total = 0
    for x,y in dirs:
        total += palin_paths(m,
                             cur_str=cur_str+m[y+cur_y][cur_x+x],
                             cur_pos=(cur_x+x, cur_y+y))
        # ok
    mem[key] = total
    return total


mat = ["aaab",
       "baaa",
       "abba"]

print(palin_paths(mat))
