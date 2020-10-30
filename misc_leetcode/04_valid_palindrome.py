'''
Created on 30 Oct 2020

@author: peter
'''


def is_a_palindrome(phrase: str) -> bool:
    
    phrase = phrase.lower()

    i = 0
    j = len(phrase) - 1

    while i < j:
        ''' while is need here as there may be more than one
        non-alpha char in succession '''
        while (i < j) and not (phrase[i].isalpha()):
            i += 1
        while (i < j) and not (phrase[j].isalpha()):
            j -= 1
        
        if phrase[i] != phrase[j]:
            return False
        
        i += 1
        j -= 1
    
    return True


if __name__ == '__main__':

    print(is_a_palindrome('A man, a plan, a canal: Panama'))
    
