from easy_trilateration.model import *  
from easy_trilateration.least_squares import easy_least_squares  
from easy_trilateration.graph import *  
import math

if __name__ == '__main__':  
    arr = [Circle(3,1, float(math.sqrt(13))),    #(x,y,r)
    Circle(1,6, float(math.sqrt(10))),
    Circle(6,6, float(math.sqrt(8)))]
    # Circle(8,2, float(math.sqrt(17)))         # 4 beacon 으로 하면 정확도 up

    result, meta = easy_least_squares(arr)
    create_circle(result, target=True)
    
    # 값 추출
    re = str(result)
    re = re.replace("Circle(","").replace(")","").replace(",","")
    x,y,r = re.split(" ")

    # draw(arr)
