print("1 = Add")
print("2 = Subtract")
print("3 = Multiply")
print("4 = Divide")
choice = int(input("Enter the operation:"))
output = 0
if choice in [1,2,3,4]:
    num1=float(input("Enter first number:"))
    num2=float(input("Enter second number:"))
    if choice==1:
        output = num1 + num2
    elif choice==2:
        output = num1 - num2
    elif choice==3:
        output = num1 * num2
    elif choice==4:
        output = num1 / num2
    
else:
    print("Invalid input")
print("The result is:",output)