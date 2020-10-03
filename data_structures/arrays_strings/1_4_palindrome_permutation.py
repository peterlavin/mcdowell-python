'''
Created on 3 Oct 2020

@author: peter
'''
from ansible.modules.identity import _onepassword_facts

def is_permutation_palindrome(phrase: str) -> bool:
    
    phrase = phrase.lower()
    
    
    
    num = 1
    num = num^0
    
    print(num)
    
    num = num^1
    num = num^1
    
    print(num)
    
    # Create a dict for count,
    counts = {}
    
    # itr over the phrase, each time a char is found,
    # if not already there, set to 1, if already there XOR with 1 (to flip it)
    for char in phrase:
        pass
    # count 1s in the dict, if count > 1, return false, else true.
    
    return True




if __name__ == '__main__':
    
    print(is_permutation_palindrome("phrase"))
    
    pass