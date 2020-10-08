'''
Created on 3 Oct 2020

@author: peter
'''

import pytest


def is_permutation_palindrome(phrase: str) -> bool:
    
    ''' Determines if a string is a perumtation of a palindrome
    by checking that, at most, only one char has an odd frequency
    Even length-strings must have all even frequencies, odd-length 
    strings can have at most one odd frequency, with this char being
    in the middle of the string '''
 
    # Remove whitespaces and make lowercase   
    phrase = phrase.replace(' ', '').lower()
        
    counts = {}
    
    for char in phrase:
        # Python pattern to avoid KeyError when a key
        # does not previously exist in a dict
        counts.setdefault(char, 0)
        # XOR or flip the previous value, we don't care
        # about the frequency, just if it is odd/even
        counts[char] = counts[char] ^ 1
        
    print(counts)
    
    ones_zeros = list(counts.values())
    print(ones_zeros)
    
    return ones_zeros.count(1) <= 1
    
    
class TestPalindromePerms():
    ''' Tests for is_permutation_palindrome '''
        
    def test_known_true(self):
        assert is_permutation_palindrome("tattarrattat") == True
        
    def test_known_false(self):
        assert is_permutation_palindrome("qwertyuiopp") == False
        
    data = [('a b c c b a', True),
            ('aaaaa', True),
            ('BBBaaa', False),
            ('Na vanxnavan', True)]

    @pytest.mark.parametrize('string, expected', data)
    def test_multiple(self, string, expected):
        assert is_permutation_palindrome(string) == expected
    
     
