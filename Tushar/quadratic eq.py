a= int(input("enter the value of a"))
b= int(input("enter the value of b"))
c= int(input("enter the value of c"))

d=(b**2-4*a*c) #discriminant
if d>0:
    sol1=(((-b+(b**2-4*a*c))**0.5)/2*a)
    sol2=(((-b-(b**2-4*a*c))**0.5)/2*a)
    print("roots of the quadratic eq are :- ",sol1 , sol2)
elif d==0:
    sol=(((-b+(b**2-4*a*c))**0.5)/2*a)
    print("the roots of the quadratic eq are :- ", sol)
else:
    print('this quradratic eq has no real roots')
