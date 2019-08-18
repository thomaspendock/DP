'''
Hedwig the hamster enjoys exploring networks of hamster tubes. Each day,
Hedwig’s owner rearranges the tubes to form a new network of tubes.


One day, Hedwig awoke to find that the network of tubes had been arranged in a
ladder pattern as shown below, where each junction point (An and Bn) contained
a small piece of carrot (Hedwig loves carrots!). Hedwig had not yet explored the
new tube network and had no idea how long it was (it may
go on forever!)

Hedwig decided to make a game where given a length, figure out how many paths
from the start, A0, of the given length there are using these rules: Each time a
junction is reached, Hedwig eats the piece of carrot that is there. A junction
can only be used if there is a piece of carrot there when Hedwig arrives.

To help Hedwig out, you will write a program which finds the number of paths
from A0 of a specified length which do not hit any junction more than once.

http://acmgnyr.org/year2018/problems/C-hed_ladder.pdf
Note: Sample output for 4 111 was changed to 4 237
'''


mem = {}
def hedwig(steps, x=0, y=0, left_x=-1, left_y=1,):

    key = steps, x, left_x, left_y
    if key in mem:
        return mem[key]

    if steps == 0:
        return 1


    total = 0
    dirs = []
    if left_y == y:
        # Move left
        if x - left_x - 1 >= steps:
            total += 1
            
        # Move right
        dirs += [[(1, 0), (x, (left_y + 1) % 2)]]
        
    else:
        # Move down/up
        dirs += [[(0, 1 + -2*y), (left_x, left_y)]]

        # Move right
        dirs += [[(1, 0), (left_x, left_y)]]

    for (dir_x, dir_y), (new_x_left, new_y_left) in dirs:
        env = {'steps': steps-1, 'x': x+dir_x, 'y': y+dir_y,
               'left_x': new_x_left, 'left_y': new_y_left}
        print(env)
        total += hedwig(steps-1, x=x+dir_x, y=y+dir_y,
                        left_x=new_x_left, left_y=new_y_left)

    mem[key] = total
    return total

# 3 ---> 6
# 9 ---> 110
# 18 --> 8361
# 111 -> 237
print(hedwig(2) % 10007)
