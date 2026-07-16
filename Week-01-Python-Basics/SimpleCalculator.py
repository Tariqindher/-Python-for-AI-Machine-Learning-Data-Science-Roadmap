try:
   num1=float(input("Enter the number: "))
   num2=float(input("Enter the number: "))
except ValueError:
    print("Invalid Input please enter the number")
    exit()
    
opr=input("choose the symbol(+,-,*,/): ")
result=0
if opr=="+":
    result=num1+num2
elif opr=="-":
    result=num1-num2
elif opr=="*":
    result=num1*num2
elif opr=="/":
    if num2!=0:
        result=num1/num2
    else:
        print("you can't divide by zero")
else:
    print("Invalid Operator")

print("Result",result)
