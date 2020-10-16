'''
Created on Oct 2020

@author: peter
'''

import pytest


def one_edit_separate(str_one: str, str_two: str) -> bool:
    
    def one_replace_away(str_one,str_two):
        ''' Strings are the same length, so if one (only)
        char is different, ret True, else False '''
        
        already_found_diff = False
        
        for i in range(len(str_one)):
            if str_one[i] != str_two[i]:
                if already_found_diff:
                    return False
                already_found_diff = True
        
        return True


    def one_insert_away(str_one,str_two):
        ''' Called when one string is 1 char longer than the other,
        therefore they can be made the same with one 'insert' '''
        
        ix_one = 0
        ix_two = 0
        
        ''' Start along the string, check chars are the same, if a char is
        different, this is ok ONCE, jump ahead one char in the longer string
        and continue checking. If a second diff is found, return False '''
        
        while(ix_one < len(str_one) and ix_two < len(str_two)):
            if str_one[ix_one] != str_two[ix_two]:
                if ix_one != ix_two:
                    return False
                ix_two +=1
            else:
                ix_one +=1
                ix_two +=1
        
        return True
    
        
    if len(str_one) == len(str_two):
        return one_replace_away(str_one, str_two)
    elif len(str_one) + 1 == len(str_two):
        return one_insert_away(str_one, str_two)
    elif len(str_two) + 1 == len(str_one):
        return one_insert_away(str_two, str_one)
    
    return False

def one_edit_combined(str_one: str, str_two: str) -> bool:
    
    ''' First up, if the strings differ in length by more
    than 1, return False '''
    
    if abs(len(str_one) - len(str_two)) > 1:
        return False
    
    ''' Get the shortest string, if equal length, it does not matter '''
    short = min([str_one, str_two], key=len)
    # TODO
    # if strings are equal, either may be returned, so we need to be 
    # sure that we are comparing both strings, not s1 and s1
    
    
    return True







if __name__ == '__main__':
    
    a = 'aaaa'
    b = 'bbbb'
    
    # print(one_edit_separate(a, b))
    print(one_edit_combined(a, b))
    pass

class TestOneEdit():
    
    data= [('aa','ab',True),
            ('abcd','abcdef',False),
            ('abcdef','abcd',False),
            ('abccd','abcd',True),
            ('abcd','abccd',True),
            ('','',True),
            ('abcdef','mnopqr', False),]
    
    
    @pytest.mark.parametrize('s1, s2, expected', data)
    def test_one_edit_separate(self, s1, s2, expected):
        assert one_edit_separate(s1, s2) == expected
        
    def test_one_edit_combined(self):
        assert one_edit_combined('aaaa', 'aaaaaa') == False