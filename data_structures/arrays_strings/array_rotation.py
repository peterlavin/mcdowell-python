'''
Created on 20 Sep 2020

@author: peter
'''
import string
from pprint import pprint as pp


def rotate_array(image: []) -> []:
    
    # depth here means how many layers in from the outside
    # until the middle is reached. If n is odd, the middle
    # value is not moved
    print('\ndepth ranges from 0 to', int(len(image) / 2))
    
    # depth always starts at 0 and then up to half the length
    for depth in range(0, int(len(image) / 2)):

        # For the outer layer, i.e. depth=0, last is
        # the hightest index in a given row, it decreases
        # as depth increases
        last = len(image) - 1 - depth
        
        for i in range(depth, last):
            # When moving around at a given depth, offset is how
            # far around we have come. It steps back 1 for each
            # lap at a given depth
            # Starting off, offset=0, or 0-0.
            # When offset is 0, the four corners of the array are shifted.
            # When offset increments, it is subtracted from the [x][] or [][y]
            # value as appropriate.
            offset = i - depth
            # save first to temp variable
            temp = image[depth][i]
            
            # left > first location
            image[depth][i] = image[last - offset][depth]
            
            # btm to left
            image[last - offset][depth] = image[last][last - offset]
            
            # right > btm
            image[last][last - offset] = image[i][last]
            
            # top > right
            image[i][last] = temp
    
    return image


    
    

if __name__ == '__main__':

    letters = string.ascii_lowercase[:26]
   
    image = []
    count = 0
    n = 4  
    for j in range(0, n):
        image.append([])
        for k in range(0, n):
            image[j].append(letters[count % 26])
            count += 1
  
    pp(image)       
    rotate_array(image)
    print()
    pp(image)
 