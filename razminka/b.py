from math import gcd 
 
# Function to reduce a fraction 
# to its lowest form
def reduceFraction(x, y) :
     
    d = gcd(x, y)
 
    x = x // d
    y = y // d
    return x,y


    

a,b,c,d = map(int, input().split())



one = a*d +c*b
two = b * d
# print('upper', a*d +c*d)
# print('down', b * d)
one, two = reduceFraction(one, two)
print(one,two)