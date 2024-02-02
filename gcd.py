a=int(input('enter the 1st no.'))
b=int(input('enter the 2nd no.'))

def gcd(a,b):
    result = min(a,b)
    while result:
        if a%result==0 and b%result==0:
            break
        result-=1
    return result
print('the gcd is:',gcd(a,b))
