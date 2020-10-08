'''
Created on 3 Oct 2020

@author: peter
'''

import pytest
from BitVector import BitVector
import string


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
    
    ''' Uses a bitvector to trace the odd or eveness of
    the frequency count for each char '''

    phrase = phrase.replace(' ', '').lower()
    print(phrase)
    
    # E.g. using intVal (integer value) of 7 would give 00...111    
    bv = BitVector(intVal=0, size=26)
    
    for char in phrase:
        # Calculate the place in alphabet for the char,
        # and flip/xor 1 the bit at that place
        ordinal = ord(char) - 96 - 1
        bv[ordinal] = bv[ordinal] ^ 1
       
    ''' Some binary number Fu... if there is only one bit set to 1, then
    the value of 'that vector minus 1' when ANDed (&) with the original
    vector will be 0. 
    E.g. 01000 - 00001 = 00111, so 01000 & 00111 = 00000''' 
    # max(..) is needed as the entire vector may be all zeros
    bv_minus_one = BitVector(intVal=max(int(bv) - 1, 0), size=26)
        
    return int(bv & bv_minus_one) == 0
    
    
class TestPalindromePerms():
    ''' Tests for is_permutation_palindrome '''
    
    data = [('a b c c b a', True),
           ('', True),  # Testing where the bitvector is all zeros
           ('aaaaa', True),
           ('BBBaaa', False),
           ('Na vanxnavan', True),  # spaces, x in the middle, uppercase
           ('gkifhurybdcdehijj', False),  # semi-random string
           ('tattarrattat', True)]  # longest palindrome in Ulysses (James Joyce)
        
    @pytest.mark.parametrize('s1, expected', data)
    def test_dictionary_soln(self, s1, expected):
        assert is_palindrome_perm_dict(s1) == expected
    
    @pytest.mark.parametrize('s1, expected', data)
    def test_bitvector_soln(self, s1, expected):
        assert is_palindrome_perm_bitvector(s1) == expected
