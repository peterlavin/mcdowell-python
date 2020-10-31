'''
Created on 31 Oct 2020

@author: peter
'''


def reverse_sentence_pythonic(sentence: str) -> str:
    
    sentence_list = sentence.split(' ')
    return ' '.join(w for w in sentence_list[::-1])


def reverse_sentence(sentence: str) -> str:

    output = ''    

    j = len(sentence)

    ''' range down to -1 to use 0 ''' 
    for i in range(len(sentence)-1, -1, -1):

        if sentence[i] == ' ':
            output += sentence[i + 1:j] + ' '
            j = i
        elif i == 0:
            output += sentence[i:j]
            
    return output


if __name__ == '__main__':
   
    sentence = 'sky is blue magnificant'
    print(sentence)
    print(reverse_sentence_pythonic(sentence))
    
    sentence = 'yesterday water was deep'
    print('\n', sentence, sep='')
    print(reverse_sentence(sentence))
