'''
Given an array a of size N and an integer K, the task is to divide the array
into K segments such that sum of the minimum of K segments is maximized.
'''

# maximize sum of minums
import random

MAX = 1000
  
# Function to maximize the sum of the minimums 
def maximizeSum(a,n, ind, k, dp): 
    # If k segments have been divided 
    if (k == 0): 
        # If we are at the end 
        if (ind == n): 
            return 0
  
        # If we donot reach the end 
        # then return a negative number 
        # that cannot be the sum 
        else: 
            return -1e9
  
    # If at the end but 
    # k segments are not formed 
    elif (ind == n): 
        return -1e9
  
    # If the state has not been visited yet 
    elif (dp[ind][k] != -1): 
        return dp[ind][k] 
  
    # If the state has not been visited 
    else: 
        ans = 0
  
        # Get the minimum element in the segment 
        mini = a[ind] 
  
        # Iterate and try to break at every index 
        # and create a segment 
        for i in range(ind,n,1): 
            # Find the minimum element in the segment 
            mini = min(mini, a[i]) 
  
            # Find the sum of all the segments trying all 
            # the possible combinations 
            ans = max(ans, maximizeSum(a, n, i + 1, k - 1, dp) + mini) 
  
        # Return the answer by 
        # memoizing it 
        dp[ind][k] = ans 
        return ans

calls = 0
mems = 0

def solution(a, k, left=0, mem={}):
    global calls, mems
    calls += 1
    
    if (left, k) in mem:
        mems += 1
        return mem[(left, k)]
    
    if k == 1:
        ans = min(a[left:])
        mem[(left, k)] = ans
        return ans
    
    largest_sum = a[left]
    current_min = a[left]
    for i in range(left+1, len(a) - ((k-1) - 1)):
        current_min = min(current_min, a[i-1])
        right_sum = solution(a, k-1, left=i)
        largest_sum = max(current_min + right_sum, largest_sum)
        
    mem[(left, k)] = largest_sum
    
    return largest_sum
 
a = [random.randint(3, 100) for i in range(1000)]
k = 10

n = len(a) 
  
# Initialize dp array with -1 
dp = [[-1 for i in range(MAX)] for j in range(MAX)] 

print(maximizeSum(a, n, 0, k, dp)) 


#a = [6, 5, 3, 8, 9, 10, 4, 7, 10]
#k = 4


print(solution(a,  k))
print(calls, mems)
