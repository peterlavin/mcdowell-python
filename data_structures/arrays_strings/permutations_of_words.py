'''
Created on 3 Oct 2020

@author: peter
'''

from itertools import permutations as per

all_perms = [''.join(letter) for letter in per(list('peterlavin'))]

print(len(all_perms))

# print(all_perms)
for i, perm in enumerate(all_perms):
    if i < 1000:
        print(perm)
    else:
        break
# 
# valid_words = ('cat', 'act', 'tac')
# 
# final_list = []
# 
# for word in all_perms:
#     if word in valid_words:
#         final_list.append(word)
# 
# 
# 
# print(final_list)

if __name__ == '__main__':
    pass