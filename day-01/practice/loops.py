#print("Hello world")
def sum():
    a = 10
    b = 10
    print("The sum of both a and b is :",a+b)


#num1 =  int(input("Enter the Number 1 :"))
#num2 = int(input("Enter the Number 2 :"))

#print("Your Number 1 is :",num1)
#print("Your Number 2 is :",num2)

#print("The Addition of both Number 1 and Number 2 is :",num1+num2)
#print("The Subtraction of both Number 1 and Number 2 is :",num1-num2)
#print("The Multiplication of both Number 1 and Number 2 is :",num1*num2)
#print("The Division of both Number 1 and Number 2 is :",num1/num2)

#y = 1
#print(type(y))
def Environments():
    for i in range(1):
        env = input("Enter the Environment: QAT / CST / PROD : ")
        print("Your input is : ",env)

        if env == "QAT":
            print("Test the product well.")
        elif env == "CST":
            print("Create a backup.")
        elif env == "PROD":
            print("Make sure it is not Friday.")
        else:
            print("Please enter the correct Environment.")

Environments()
sum()