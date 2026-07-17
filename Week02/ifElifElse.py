#Concepts Covered:
#✅ if
#✅ elif
#✅ else
#✅ Nested if
try:
    marks = int(input("Enter Marks (0-100): "))

    if marks < 0 or marks > 100:
        print("Invalid Marks")
        exit()

except ValueError:
    print("Invalid Marks")
    exit()

if marks >= 40:
    print("Pass")

    if marks >= 90:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: B")
    elif marks >= 70:
        print("Grade: C")
    elif marks >= 60:
        print("Grade: D")
    else:  # 40–59
        print("Grade: E")

else:
    print("Fail")
    print("Grade: F")
