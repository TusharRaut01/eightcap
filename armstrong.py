num= int(input('enter the no'))
sum =0
temp = num
power = len(str(num))
while temp>0:
    digit = temp%10
    sum+= digit**power
    temp=temp//10

if num==sum:
    print(num,"is an armstrong no")
else:
    print(num,"is not an armstrong no.")