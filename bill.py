bill = 0
running = 0
owedAmount = 0
roundedAmount = 0
while running <= 49:
    quality = input("Thanks for dining with us today! How was our service today? Was it bad, okay, good, or great? ")
    if quality == "bad" or quality == "Bad":
        print("We're so sorry. ")
        bill = 1
        print(f"We suggest tipping your server 0% of your bill.")
        running = 100
    elif quality == "okay" or quality == "Okay" or quality == "ok" or quality == "Ok" or quality == "OK":
        print("We're sorry if the service did not meet your expectations. ")
        bill = 1.15
        print(f"We suggest tipping your server 15% of your bill.")
        running = 100
    elif quality == "good" or quality == "Good":
        print("Thank you for the rating!")
        bill = 1.20
        print(f"We suggest tipping your server 20% of your bill.")
        running = 100
    elif quality == "great" or quality == "Great":
        print("Thank you for the exceptional rating!")
        bill = 1.25
        print(f"We suggest tipping your server 25% of your bill.")
        running = 100
    else:
        print("I'm sorry, something went wrong. Try again. ")
        running = 25
owedAmount = float(input("What's your bill amount? Don't use the dollar sign. "))
newAmount = owedAmount * bill
roundedAmount = round(newAmount, 2)
print(f"Your suggested bill is ${roundedAmount}.")