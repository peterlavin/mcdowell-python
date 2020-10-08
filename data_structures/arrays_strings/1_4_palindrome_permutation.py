'''
Created on 3 Oct 2020

@author: peter
'''

import pytest
from BitVector import BitVector


def is_palindrome_perm_dict(phrase: str) -> bool:
    
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
   
    ones_zeros = list(counts.values())
    
    return ones_zeros.count(1) <= 1
    
    
def is_palindrome_perm_bitvector(phrase: str) -> bool:

    phrase = phrase.replace(' ', '').lower()
    
    # E.g. using intVal (integer value) of 8 would give 1000    
    bv = BitVector(intVal=0, size=26)
    print(bv)

    for char in phrase:
        # Calculate the place in alphabet for the lc char
        ordinal = ord(char) - 96 - 1
        bv[ordinal] = bv[ordinal] ^ 1
               
    print(bv)
    
    # Subtract 1 from this bitvector
    bv_minus_one = BitVector(intVal=int(bv)-1, size=26)
    print(bv_minus_one)
    print(bv & bv_minus_one)
    print(bv ^ bv_minus_one)
    
    # Some bitvector Fu
    return int(bv & bv_minus_one) == 0
    

print(is_palindrome_perm_bitvector("abcdefghijklm"))
    
    
class TestPalindromePerms():
    ''' Tests for is_permutation_palindrome '''
    
    data = [('a b c c b a', True),
           ('aaaaa', True),
           ('BBBaaa', False),
           ('Na vanxnavan', True)]
        
    def test_known_true(self):
        assert is_palindrome_perm_dict("tattarrattat") == True
        
    def test_known_false(self):
        assert is_palindrome_perm_dict("qwertyuiopp") == False

    @pytest.mark.parametrize('string, expected', data)
    def test_multiple(self, string, expected):
        assert is_palindrome_perm_dict(string) == expected
     
