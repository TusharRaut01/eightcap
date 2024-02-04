num=int(input('enter the no.'))

def factor(num):
    print('the factor of the',num ,'is')
    for i in range(1,num+1):
        if num % i ==0:
            print(i)
print(factor(num))

