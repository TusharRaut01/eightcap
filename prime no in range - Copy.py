lower = 0
num = int(input('enter the no'))

print("Prime numbers between", lower, "and", num, "are:")

for num in range(lower, num + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
    