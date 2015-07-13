# -*- coding: utf-8 -*-
# Author: Jing Chen @ EMC Corp. jing.chen2@emc.com
#

import math

def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

def dis(x_in, y_in, x_ref, y_ref):
    return math.sqrt((x_in-x_ref)**2 + (y_in-y_ref)**2)
        
def Trilateration(x1,y1,d1,x2,y2,d2,x3,y3,d3):
    '''
    Distances (d1,d2,d3) are measured by an RSSI signal.
    (x1,y1), (x2,y2) and (x3,y3) are locations of the three APs.
    (x,y) is the returned calculated location of the receiver. 
    '''
    a1x = 2*(x2-x1)
    b1y = 2*(y2-y1)
    c1  = (d1**2-d2**2)-(x1**2-x2**2)-(y1**2-y2**2)
    a2x = 2*(x3-x1)
    b2y = 2*(y3-y1)
    c2  = (d1**2-d3**2)-(x1**2-x3**2)-(y1**2-y3**2)
    x = (c1*b2y-c2*b1y)/(a1x*b2y-a2x*b1y)
    y = (a1x*c2-a2x*c1)/(a1x*b2y-a2x*b1y)
    return (x,y)

def Trilateration_scan(x1,y1,d1,x2,y2,d2,x3,y3,d3,X_Min,X_Max,Y_Min,Y_Max):
    '''
    Distances (d1,d2,d3) are measured by an RSSI signal.
    (x1,y1), (x2,y2) and (x3,y3) are locations of the three APs.
    (x,y) is the returned calculated location of the receiver. 
    '''
    isInnerLoopBreak = False
    for x in my_range(X_Min,X_Max,0.1):
        for y in my_range(Y_Min,Y_Max,0.1):
            #print x,y, dis(x,y,x1,y1), dis(x,y,x2,y2), dis(x,y,x3,y3)
            if ( abs(d1 - dis(x,y,x1,y1)) < 0.1 ) and ( abs(d2 - dis(x,y,x2,y2)) < 0.1 ) and ( abs(d3 - dis(x,y,x3,y3)) < 0.1 ):
                print "found", x, y
                isInnerLoopBreak = True
                break
        if isInnerLoopBreak:
            break
    return (x,y)


if __name__ == '__main__':
    # d1 = 280.94
    # d2 = 843.55
    # d3 = 119.19
    
    d1 = 280.94
    d2 = 843.55
    d3 = 119.19
    
    myX_Min = 1
    myX_Max = 801
    myY_Min = 1
    myY_Max = 401
    
    x1 = 1
    y1 = 1
    x2 = 801
    y2 = 1
    x3 = 1
    y3 = 401
    
    print "Tri", Trilateration(x1,y1,d1,x2,y2,d2,x3,y3,d3)
    print "Tri_scan", Trilateration_scan(x1,y1,d1,x2,y2,d2,x3,y3,d3,myX_Min,myX_Max,myY_Min,myY_Max)
