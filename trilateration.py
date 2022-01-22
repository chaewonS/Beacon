from easy_trilateration.model import *  
from easy_trilateration.least_squares import easy_least_squares  
from easy_trilateration.graph import *  
import math

if __name__ == '__main__':  
    arr = [Circle(3,1, float(math.sqrt(8))),    #(x,y,r)
    Circle(1,6, float(math.sqrt(15))),
    Circle(6,6, float(4))]
    # Circle(8,2, float(math.sqrt(17)))]

    result, meta = easy_least_squares(arr)
    create_circle(result, target=True)
    print(result)
    draw(arr)
