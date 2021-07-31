import math
a = int(input("type first rid1:" ))
b = int(input("type second rid2:" ))
c = int(input("type the third rid3:" ))


if a*a == b*b + c*c or b*b == c*c + a*a or c*c == a*a + b*b:
 print("right")


else:
 print("incorrect")  
