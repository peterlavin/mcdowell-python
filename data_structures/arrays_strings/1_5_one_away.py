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
    ''' Called when one string is 1 char longer than the other,
    therefore they can be made the same with one 'insert' '''
    
    index_one = 0
    index_two = 0
    
    ''' Start along the string, check chars are the same, if a char is
    different, this is ok ONCE, jump ahead one char in the longer string
    and continue checking. If a second diff is found, return False '''
    
    while(index_one < len(str_one) and index_two < len(str_two)):
        if str_one[index_one] != str_two[index_two]:
            if index_one != index_two:
                return False
            index_two +=1
        else:
            index_one +=1
            index_two +=1
    
    return True
    


if __name__ == '__main__':
    
    print(one_edit_away('onlcy', 'only')) # this is wrong !!!
    pass
