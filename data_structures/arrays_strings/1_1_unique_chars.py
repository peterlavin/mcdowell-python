'''
Created on 16 Sep 2020

@author: peter
'''
import pytest

def string_has_unique_chars(inp: str) -> bool:
    
    char_set = set()
    
    for ch in inp:
        if ch in char_set:
            return False
        char_set.add(ch)
        
    return True

def unique_by_sorting(inp: str) -> bool:
    
    sorted_inp = sorted(inp)
    
    for i in range(len(sorted_inp)-1):
        if sorted_inp[i] == sorted_inp[i+1]:
            return False
    return True
    
def using_list_and_set(inp: str) -> bool:
    """ Determines unique chars using the unique property
    of a set """
    inp_list = list(inp)
    inp_set = set(inp)
    return len(inp_list) == len(inp_set)
    
class TestUniqueChars():
    
    @pytest.mark.parametrize('inp,expected',[
                            ('abcdee',False),
                            ('fghijk',True),
                            ('  ',False),
                            ('',True),])
    def test_find_rep_char(self,inp,expected):
        assert string_has_unique_chars(inp) == expected
    
    
    @pytest.mark.parametrize('inp,expected',[
                            ('nfjighyy',False),
                            ('asdfghj',True),
                            ('',True),
                            ('  ',False),])
    def test_unique_by_sorting(self,inp,expected):
        assert unique_by_sorting(inp) == expected
        
    @pytest.mark.parametrize('inp,expected',[
                            ('wertyuio',True),
                            ('dfghjkll',False),
                            (' ',True),
                            ('  ',False),])
    def test_using_list_and_set(self,inp,expected):
        assert using_list_and_set(inp) == expected
    
if __name__ == '__main__':
    pass