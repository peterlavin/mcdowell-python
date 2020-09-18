'''
Created on 18 Sep 2020

@author: peter
'''


def reverse_in_place(for_reversal: str) -> str:
    """ Manual approach which reverses the string in 
    a list """
    s_list = list(for_reversal)

    start = 0
    end = s_list.__len__() - 1

    while(start < end):
        """ Convenient Python way to swap without a temp val """
        s_list[start], s_list[end] = s_list[end], s_list[start]
        start += 1
        end -= 1
    
    return ''.join(s_list)


def built_in_reverse(for_reversal: str) -> str:
    """ Slice string from end to start, 1 pos at at time """
    return for_reversal[::-1]

class TestReverseInPlace():
    
    def test_reverse_in_place(self):
        assert reverse_in_place('poiuytrewq') == 'qwertyuiop'
        assert reverse_in_place('1234 5678') == '8765 4321'
        assert reverse_in_place('') == ''
        assert reverse_in_place(' ') == ' '
        assert built_in_reverse(
            'The quick brown fox jumped over the lazy dogs') == \
            ('sgod yzal eht revo depmuj xof nworb kciuq ehT')
        
    def test_built_in_reverse(self):
        assert built_in_reverse('poiuytrewq') == 'qwertyuiop'
        assert built_in_reverse(
            'The quick brown fox jumped over the lazy dogs') == \
            ('sgod yzal eht revo depmuj xof nworb kciuq ehT')
            