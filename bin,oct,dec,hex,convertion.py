print("""1: dec to binary 
2: dec to octal  
3: dec to hexadecimal""")
num=int(input('enter the option:'))
value=int(input('enter the no'))
if num==1:
    print(bin(value),'output in binary')
elif num==2:
    print(oct(value),'output in octal')
else:
    print(hex(value),'output in hexadecimal')