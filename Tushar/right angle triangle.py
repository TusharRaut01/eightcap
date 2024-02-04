num = int(input("Enter number of num: "))

for i in range(num):
    for j in range(i+1):
        print("* ", end="")
    print("\n")