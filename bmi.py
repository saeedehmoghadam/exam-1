import math
h = float(input("type height ="))
w = float(input("type weight ="))

bmi =(h ** 2) / w  

if bmi < 18.5 :
     print("weight dificiency" )

elif 18.5 > bmi < 24.5 : 
    print ("normal")

elif 25 > bmi < 29.9 :
     print ("overwieght")

elif bmi > 30 :
     print("chubby")