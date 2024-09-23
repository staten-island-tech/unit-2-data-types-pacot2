num1 = int(input("Input one number... "))
num2 = int(input("Input a second number... "))
gcf = 1

if num1 == num2:
    print(f"The greatest common factor of {num1} and {num2} is {num1}. They're the same number!")
else:
    for i in range(1, min(num1, num2)):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
    if gcf == 1:
        print(f"The greatest common factor between {num1} and {num2} is 1.")
        print("This means that your two numbers essentially do not share any common factors.")
        print("... other than 1, of course.")
    else:
        print(f"The greatest common factor of {num1} and {num2} is {gcf}.")