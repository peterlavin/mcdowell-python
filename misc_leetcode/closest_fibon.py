'''
Created on 2 Nov 2020

@author: peter
'''

''' Determine the nearest Fibonacci number to a given number with Binet's formula '''

import math


def f(n):
    
    # sqrt of 5
    sqrt_5 = 5 ** .5
    
    # Calculates golden ratio 1.681...
    golden_ratio = .5 + sqrt_5 / 2
    print(golden_ratio)
    
    ''' log part... the golden_ratio is the log base here
    sqrt_5*n is the numeric value for getting the log of '''
    log_val = (golden_ratio ** int(math.log(sqrt_5 * n, golden_ratio))) / sqrt_5
    
    print(f'l... {log_val}')
    print(f'gr*l... {golden_ratio * log_val}')
    L = [log_val, golden_ratio * log_val]
    print([2 * n > sum(L)])

    print(L[False])
    
    return round(L[2 * n > sum(L)])


if __name__ == '__main__':
 
    print(f(4172))
    
