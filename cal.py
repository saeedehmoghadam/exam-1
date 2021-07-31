import math

number_1 = int(input("Enter your the first number: "))
number_2 = int(input("Enter your the second number: "))

y = input ( '''
 choose one of the under wiki :
+   addition
-   subtraction
*   multiplication
/   division
**  power
fac  factorial
sin  sinus
cos  cosinus
tan   tangant
radi   sqrt 
''' )

if  y == '+' :
    y_number = number_1 + number_2
    print(number_1, number_2, y_number) 

elif y == '-' :

     y_number = number_1 - number_2
     print(number_1, number_2, y_number)   
     
elif y == '*' :
     y_number = number_1 * number_2
     print(number_1, number_2, y_number)

elif y == '/' :
     y_number = number_1 / number_2
     print(number_1, number_2, y_number)   

elif  y == '**' :
    y_number = number_1 ** number_2
    print(number_1, number_2, y_number) 

elif  y == 'fac' :
    y_number = math.factorial(number_1)
    print(number_1, y_number) 

elif  y == 'sin' :
    y_number = math.sin(number_1)  
    print(number_1, y_number) 

elif  y == 'cos' :
    y_number = math.cos(number_1) 
    print((number_1, y_number) 

elif  y == 'tan' :
    y_number = math.tan(number_1) 
    print(number_1, y_number) 

elif  y == 'radi' :
    y_number = math.sqrt( number_1) 
    print(number_1, y_number) 
 else 
  print ("run again")    
