def get_dp_func(base_case_func, gen_options_func, get_acc_func, acc_init):
    """
    Returns a dp problem solving function based on some sub functions specifc to
    the problem.
    """
    
    def dp_func(mem={},
                base_case=base_case_func,
                gen_options=gen_options_func,
                get_acc=get_acc_func,
                env={}):
        
        key = tuple(env.items())
        
        # Use mem
        if key in mem:
            return mem[key]
        
        # Base Case
        if base_case(env) != None:
            return base_case(env)


        # Solve
        acc = acc_init
        options, acc = gen_options(env, acc)

        for o in options:
            sub_sol = dp_func(env=o)
            acc = get_acc(acc, sub_sol)

        mem[key] = acc
        return acc
    
    return dp_func

if __name__ == '__main__':
    ### Define input functions for hedwig's ladder ###

    base_case_hedwig = lambda env: 1 if env['steps'] == 0 else None

    def gen_options_hedwig(env, acc):
        
        dirs = []
        if env['left_y'] == env['y']:
            # Move left
            if env['x'] - env['left_x'] - 1 >= env['steps']:
                acc += 1
            # Move right
            dirs.append({'x': 1+env['x'], 'y': env['y'], 'left_x': env['x'],
                         'left_y': (env['left_y'] + 1) % 2,
                         'steps': env['steps'] - 1})
            
        else:
            # Move down/up
            dirs.append({'x': env['x'], 'y': 1 + -1*env['y'], 'left_x': env['left_x'],
                         'left_y': env['left_y'], 'steps': env['steps'] - 1})
            # Move right
            dirs.append({'x': env['x']+1, 'y': env['y'], 'left_x': env['left_x'],
                         'left_y': env['left_y'], 'steps': env['steps'] - 1})

            
        return dirs, acc   
        
    acc_func_hedwig = lambda acc, ans: acc + ans


    hedwig_ladder = get_dp_func(base_case_hedwig,
                                gen_options_hedwig,
                                acc_func_hedwig,
                                0)

    args_hedwig = {'steps': 18, 'x': 0, 'y': 0, 'left_x': -1, 'left_y': 1}
    print(hedwig_ladder(env=args_hedwig))


    ### Minimum number of partitions of a string such that each sub string is a palindrome ###

    base_case_palin = lambda env: 0 if env['s'][::-1] == env['s'] else None

    def gen_options_palin(env, acc):

        options = []
        for i in range(1, len(env['s'])+1):
            sub = env['s'][:i]
            if sub[::-1] == sub:
                options.append({'s':env['s'][i:]})
        
        return options, acc   
        
    acc_func_palin = lambda acc, ans: min(acc, ans+1)


    palin_parts = get_dp_func(base_case_palin,
                                gen_options_palin,
                                acc_func_palin,
                                10**10)

    args_palin = {'s': 'ababbbababbbababaaaaaabbbbaaaa'}
    print(palin_parts(env=args_palin))
