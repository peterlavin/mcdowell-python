'''
Created on 30 Oct 2020

@author: peter
'''


def find_needle(long, short):

    for i in range(len(long) - len(short) + 1):
        if long[i:i + len(short)] == short:
            return i


ans = find_needle('xyzabcuvw', 'vw')
print('\nIndex where substring starts:', ans)
        
