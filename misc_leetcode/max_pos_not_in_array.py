'''
Created on 2 Nov 2020

@author: peter
'''

''' Return the smallest positive integer GT zero that does not occur in a given array '''


def simple(A):
  
    # Find max manually for this exercise
    max_a = A[0]
    for i in range(0, len(A)):
        if A[i] > max_a:
            max_a = A[i]
    
    ret_val = max_a + 1
    
    for j in range(max_a,-1,-1 ):
        
        if j not in A and j != 0:
            return j
        
    return ret_val
    
    


def using_set(A):
    
    a = set(A)
    ans = 1  # default answer, GT 0, always increment
    
    ''' From 1, increment ans until it is not found '''
    while ans in a:
        ans += 1
        
    return ans

if __name__ == '__main__':
    
    inp = [-2, -1, 0, 1, 3, 2, 5, 6, 7, 8, -5]
    inp = [0, 1, 2, 3, 4, 5, 6, 8,-1,-3]
    
    
    print(simple(inp))
    print(using_set(inp))
