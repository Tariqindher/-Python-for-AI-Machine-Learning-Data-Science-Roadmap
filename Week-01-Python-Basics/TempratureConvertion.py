try:
   temp=float(input("Enter the temperature value: "))
except ValueError:
    print("Invalid Input please enter the number")
    exit()
print("choose conversion\n1.Celsius to Fahrenheit\n2.Fahrenheit to Celsius\n3.Celsius to Kelvin \n4.Kelvin to Celsius")
choice=int(input("Enter the choice "))

if choice==1:
    result = (temp * 9/5) + 32
    print("Temperature in Fahrenheit:", result, "°F")
elif choice==2:
    result = (temp - 32) * 5/9
    print("Temperature in Celsius:", result, "°C")
elif choice==3:
    result = temp + 273.15
    print("Temperature in Kelvin:", result, "K")
elif choice==4:
    result = temp - 273.15
    print("Temperature in Celsius:", result, "°C")
else:
    print("Invalid choice")
