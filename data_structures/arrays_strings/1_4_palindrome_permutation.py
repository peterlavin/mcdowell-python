'''
Created on 3 Oct 2020

@author: peter
'''
from ansible.modules.identity import _onepassword_facts

def is_permutation_palindrome(phrase: str) -> bool:
    
    phrase = phrase.lower()
    
    
   
    # Create a dict for count,
    counts = {}
    
    # itr over the phrase, each time a char is found,
    # if not already there, set to 1, if already there XOR with 1 (to flip it)
    for char in phrase:
        counts.setdefault(char, 0)
        #counts[char] += 1
        counts[char] = counts[char]^1
        
    print(counts)
        
    print(list(counts.values()))
    
    limit_of_one = False
    
    for num in list(counts.values()):
        if num % 2 != 0 and limit_of_one:
            return False
        else:
            limit_of_one = True
    
    return True



if __name__ == '__main__':
    
    print(is_permutation_palindrome("navanxnavan"))
    
    print(is_permutation_palindrome("tattarrattat"))
    
    
    pass