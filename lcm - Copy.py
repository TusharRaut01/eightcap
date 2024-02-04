a=int(input('enter the 1st no.'))
b=int(input('enter the 2nd no.'))

def lcm(a,b):
    result = max(a,b)
    while result:
        if result % a == 0 and result % b == 0:
            lcm = result
            break
        result+=1
    return result
print('the lcm is:',lcm(a,b))