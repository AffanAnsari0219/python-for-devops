a = int(input("Enter the Number 1: "))
b = int(input("Enter the Number 2: "))
print(type(a))

print("The Multiplication of a and b is : ",a*b)
print("The Addition of a and b is : ",a+b)
print("The Subrtaction of a and b is : ",a-b)

env = input("Enter the Environment : ")
print("The user input is : ",env)

if env == "prod":
    print("Do not deploy on friday")
elif env == "cst":
    print("Take backup")
else :
    print("Safe to deploy")