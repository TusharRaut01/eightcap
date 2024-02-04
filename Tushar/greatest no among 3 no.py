a = int(input('enter the 1st no.'))
b = int(input('enter the 2nd no.'))
c = int(input('enter the 3rd no.'))
if a>b and a>c:
    print(a, "is greater among ",b ,c)
elif a<b and b>c:
    print(b, "is greater among ",a  ,c)
else:
    print(c, "is greater among ",a ,b)