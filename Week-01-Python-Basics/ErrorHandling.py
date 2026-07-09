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
