#exercice 2
import math

n = float(input("Enter a number : "))
char = input("Enter a char (+, -, *, /, %, square, root) : ")
p = float(input("Enter a number : "))

if (char == '+') :
    print (n, '+', p, '=', n+p)
elif (char == '-') : 
    print (n, '-', p, '=', n-p)
elif (char == '*') :
    print (n, '*', p, '=', n*p)
elif (char == '/') :
    if (p>0 or p<0) :
        print (n, '/', p, '=', n/p)
    elif (p==0) :
        print("error")
elif (char == 'mod') :
    print (n, '%', p, '=', n%p)
elif (char == 'root') :
    print ('root of', n, '=', math.sqrt(n))
elif (char == 'square') :
    print ('square of', n, '=', math.pow(n,p))