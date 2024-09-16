bill = 0
running = 0
while running <= 49:
    quality = input("Thanks for dining with us today! How was our service today? Was it bad, okay, good, or great? ")
    if quality == "bad" or quality == "Bad":
        print("We're so sorry. ")
        bill = 0
        print(f"We suggest tipping your server {bill}% of your bill.")
        break
    elif quality == "okay" or quality == "Okay" or quality == "ok" or quality == "Ok" or quality == "OK":
        print("We're sorry if the service did not meet your expectations. ")
        bill = 15
        print(f"We suggest tipping your server {bill}% of your bill.")
        break
    elif quality == "good" or quality == "Good":
        print("Thank you for the rating!")
        bill = 20
        print(f"We suggest tipping your server {bill}% of your bill.")
        break
    elif quality == "great" or quality == "Great":
        print("Thank you for the exceptional rating!")
        bill = 25
        print(f"We suggest tipping your server {bill}% of your bill.")
        break
    else:
        print("I'm sorry, something went wrong. Try again. ")
        running = int(running + 1)
if running == 50:
    print("Why are you inputting so much? Please stop... Come back when you've learned some patience.")