'''
Created on 30 Oct 2020

@author: peter
'''


def find_needle(long, short):
    
    if len(long) < len(short):
        return -1

    for i in range(len(long) - len(short) + 1):
        if long[i:i + len(short)] == short:
            return i

    return -1

if __name__ == '__main__':
    
    long  = 'the quick brown fox jumped over the lazy dogs'
    short = 'jump'
    
    ans = find_needle(long, short)
    print('\nIndex where substring starts:', ans)
    
    if ans != -1:
        print('-'*ans, short, '-'*(len(long)-len(short)-ans),'\n',long,  sep='')
    else:
        print('0'* len(long), '\n', long, sep='')
