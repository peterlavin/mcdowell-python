'''
Created on 20 Sep 2020

@author: peter
'''
import string
from pprint import pprint as pp


def rotate_array(image: []) -> []:
    """ Rotates an array in place, assumes the array will be square"""
    
    # depth here means how many layers in from the outside
    # until the middle is reached. If n is odd, the middle
    # value is not moved. Depth will range from 0 to half
    # of the length or an array side
    for depth in range(0, int(len(image) / 2)):

        # last is the hightest index in a given row,
        # it decreases as depth increases
        last = (len(image) - 1) - depth
        
        for i in range(depth, last):
            # When moving around at a given depth, offset is how
            # far around we have come. It steps back 1 for each
            # lap at a given depth
            # Starting off at each depth, offset=0,
            # When offset is 0, the four corners of the array are shifted.
            # When offset increments, it is subtracted from the [x][] or [][y]
            # value as appropriate.
            offset = i - depth
            
            # save top left to temp variable
            temp = image[depth][i]
            
            # to right moves to top left  (0,0) < (n,0)
            image[depth][i] = image[last - offset][depth]
            
            # btm right to top right (n,0) < (n,n)
            image[last - offset][depth] = image[last][last - offset]
            
            # btm left to btm right (n,n) < (0,n)
            image[last][last - offset] = image[i][last]
            
            # temp < (0,n)
            image[i][last] = temp
    
    return image


    
    

if __name__ == '__main__':

    letters = string.ascii_lowercase[:26]
   
    image = []
    count = 0
    n = 5 
    for j in range(0, n):
        image.append([])
        for k in range(0, n):
            image[j].append(letters[count % 26])
            count += 1
  
    pp(image)       
    rotate_array(image)
    print()
    pp(image)
 