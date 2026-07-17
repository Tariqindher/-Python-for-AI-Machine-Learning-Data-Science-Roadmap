for num in range(1, 21):

    # Stop when number reaches 18
    if num == 18:
        break

    # Skip numbers divisible by 4
    if num % 4 == 0:
        continue

    # Check if number is even or odd
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")

    # Nested if to check for prime numbers
    if num > 1:
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print("Prime")
