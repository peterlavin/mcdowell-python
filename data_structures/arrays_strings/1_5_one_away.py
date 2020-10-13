'''
Created on Oct 2020

@author: peter
'''


def one_edit_away(str_one: str, str_two: str) -> bool:
    
    if len(str_one) == len(str_two):
        return one_replace_away(str_one, str_two)
    elif len(str_one) + 1 == len(str_two):
        return one_insert_away(str_one, str_two)
    elif len(str_two) + 1 == len(str_one):
        return one_insert_away(str_two, str_one)
    
    return False
    
    
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
    return True
    
    pass


if __name__ == '__main__':
    
    print(one_edit_away('oooy', 'only'))
    pass
