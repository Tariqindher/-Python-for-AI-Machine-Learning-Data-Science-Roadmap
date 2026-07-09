#Error Vs Exception
#Error: An issue in the prgram that stop the execution. (Exp: Syntax Error)
#Exception: A run time issue in the prgram that can stop our program. (exp: indexerror , divison error etc)

Example Code Structure:
try:  
    # Potentially problematic operation  
except SomeException:  
    # Handling exception  
else:  
    # Executed if try is successful  
finally:  
    # Cleanup code that always runs

#Concept in Exception handling
#1. Try Block :The try block contains code that might cause an error.The try block contains code that might cause an error.
#2. Except Block : The except block handles the error so the program doesn't crash.
#3. Else Block :   The else block runs only if no exception occurs.
#4. Finally Block: The finally block always executes, whether an exception occurs or not.
#5. Raised Statement :The raise statement is used to create (raise) an exception manually.

#if the user entered number it run else block otherwise run except block 
try:
    num=int(input("Please enter the Number : "))
    #if user enter abc it raises a ValueError and goes to except
except ValueError:
    print("Invalid input. Please enter a number")
else: 
    print("You  entered: ",num)
finally:
    print("It is always run ")
#Raise Statemnt
age = int(input("Enter your age"))

if age < 18:
    raise ValueError("Age must be 18 or older ")
print("This Code will run  when age>=18.")

#Multiple exception examples
try:
    num = int(input("Enter a number: "))
    result = 10 / num

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result =", result)

finally:
    print("Program finished.")



