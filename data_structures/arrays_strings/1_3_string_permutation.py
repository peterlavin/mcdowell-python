'''
Created on 18 Sep 2020

@author: peter

Points to look out for...
 * Case sensitivity
 * Whitespace sensitivity
 
 ** All approaches assume all chars are lower case **
'''
import pytest


def is_permutation(s1: str, s2: str) -> bool:
    
    s1 = s1.replace(' ', '')
    s2 = s2.replace(' ', '')
    
    """ For starters, if strings are unequal length, they cannot
    be an anagram """
    if len(s1) != len(s2):
        return False
    """ Removes white spaces before sorting """
    return sorted(s1) == sorted(s2)
    
def is_permutation_by_char_count(s1: str, s2: str) -> bool:
    
    """ White space are replaced as spaces as keys
    are not backward compatible """
    s1 = s1.replace(' ', '_')
    s2 = s2.replace(' ', '_')
    
    """ Count chars in each string, iterate over one string
    and check for a different char-count """
    s1_char_count = {}
    s2_char_count = {}
    
    for char in s1:
        s1_char_count.setdefault(char, 0)
        s1_char_count[char] += 1
        
    for char in s2:
        s2_char_count.setdefault(char,0)
        s2_char_count[char] += 1
    
    print(s1_char_count)
    print(s2_char_count)
    
    """ Unequal length means false, also, we only check s1 against s2,
    and if s2 has chars not in s1, the below loop will not catch this """
    if len(s1_char_count) != len(s2_char_count):
        return False
    
    """ s2 may be a subset of s1,
    we need to check if all s1 chars are in s2 """
    for char,count in s1_char_count.items():
        if not (char in s2_char_count and s2_char_count[char] == count):
            return False
    
    return True
        
    
class TestPermutations():
    """ Tests are not comprehensive """

    data= [('conversation','voicerantson',True),
           ('abcd','abcde',False),
           ('abcdee','abcde',False),
           ('abc def','abcd ef',True),]
    
    @pytest.mark.parametrize('s1, s2, expected', data)
    def test_is_permutation(self,s1,s2,expected):
        assert is_permutation(s1, s2) == expected
    
    @pytest.mark.parametrize('s1, s2, expected', data)
    def test_is_permutation_by_char_count(self,s1,s2,expected):   
        assert is_permutation_by_char_count(s1,s2) == expected
