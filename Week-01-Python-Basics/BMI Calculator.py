try:
   weighet=float(input("Enter weight in kg : "))
   heighet=float(input("Enter heighetin meters : "))
except ValueError:
    print("Invalid Input please enter the number")
    exit()
bmi=weighet/(heighet*heighet)
print("BMI: ",bmi)
if bmi<18.5:
    print("Underweight")
elif bmi>=18.5 and bmi<=24.9:
    print("Normal weighet")
elif bmi>=25 and bmi<=29.9:
    print("Underweighet")
