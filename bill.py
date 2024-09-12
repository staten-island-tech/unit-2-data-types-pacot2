bill = 0
quality = input("Thanks for dining with us today! How was our service today? Was it bad, okay, good, or great? ")
if quality == "bad" or quality == "Bad":
    print("We're so sorry. ")
    bill = 0
    print(f"We suggest tipping your server {bill}% of your bill.")
elif quality == "okay" or quality == "Okay" or quality == "ok" or quality == "Ok" or quality == "OK":
    print("We're sorry if the service did not meet your expectations. ")
    bill = 15
    print(f"We suggest tipping your server {bill}% of your bill.")
elif quality == "good" or quality == "Good":
    print("Thank you for the rating!")
    bill = 20
    print(f"We suggest tipping your server {bill}% of your bill.")
elif quality == "great" or quality == "Great":
    print("Thank you for the exceptional rating!")
    bill = 25
    print(f"We suggest tipping your server {bill}% of your bill.")
else:
    print("I'm sorry, something went wrong. Try again. ")