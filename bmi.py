import math
h= int(input("please input height : "))
w= int(input(" please input weight :"))

hei = (h * 100) ** 2

bmi = w / hei

if 25<= bmi < 30 :      
    print("fat")

elif  18<= bmi <25 :
    print("normal")

elif 18> bmi:
    print("bony")

elif 30<= bmi <40:
    print("very fat") 
