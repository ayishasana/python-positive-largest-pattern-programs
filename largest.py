n1 = int(input("Enter a number : "))
n2 = int(input("Enter a number : "))
n3 = int(input("Enter a number : "))

if (n1 >= n2) and (n1 >= n3):
    print("Largest number is {}".format(n1))
elif (n2 >= n1) and (n2 >= n3):
    print("Largest number is {}".format(n2))
else:
    print("Largest number is {}".format(n3))