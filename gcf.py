num1 = int(input("Input one number... "))
num2 = int(input("Input a second number... "))
gcf = 1

if num1 == num2:
    print(f"The greatest common factor of {num1} and {num2} is {num1}.")
else:
    for i in range(1, max(num1, num2)):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
    print(f"The greatest common factor of {num1} and {num2} is {gcf}.")