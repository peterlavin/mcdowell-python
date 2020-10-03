'''
Created on 3 Oct 2020

@author: peter
'''

from itertools import permutations as per

all_perms = [''.join(letter) for letter in per(list('cat'))]

print(all_perms)

if __name__ == '__main__':
    pass