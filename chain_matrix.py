from generic_dp import get_dp_func
import numpy as np
        
    
base_case = lambda env: np.product(env['m_list']) if len(env['m_list']) == 3 else None


def recursion_step(env, acc):
    m_list = env['m_list']

    # pick two to multiply
    # figure out new dimensions and number of calcs
    # edit the list
    # calcs + min_step

    nexts = []
    
    for i in range(0, len(m_list)-2):
        calcs = m_list[i] * m_list[i+1] * m_list[i+2]
        new_m_list = m_list[:i+1] + m_list[i+2:]

        nexts.append({'calc': calcs, 'm_list': new_m_list})

    return nexts, acc

#acc = lambda acc, ans: 
        


def chain_matrix(a, mem={}):

    key = tuple(a)
    
    if key in mem:
        return mem[key]

    if len(a) == 3:
        return np.product(a)


    min_calcs = 10**10

    for i in range(len(a)-2):
        sub_calcs = np.product(a[i:i+3])
        new_list = a[:i+1] + a[i+2:]
        calcs = sub_calcs + chain_matrix(new_list)
        
        min_calcs = min(calcs, min_calcs)

    mem[key] = min_calcs
    return min_calcs

al = [40, 20, 30, 10, 30]
print(chain_matrix(al))
        
