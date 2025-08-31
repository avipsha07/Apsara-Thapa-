num = int(input("Enter an integer: "))

if num == 0:
    print("The number is zero.")
elif num > 0 and num % 2 == 0:
    print("The number is a positive even number.")
elif num > 0 and num % 2 != 0:
    print("The number is a positive odd number.")
elif num < 0 and num % 2 == 0:
    print("The number is a negative even number.")
else:
    print("The number is a negative odd number.")