verb1 = input("Choose one verb.")
verb2 = input("Choose another verb.")
if verb1 == verb2:
    print("Please do not choose the same verb twice!")
else:
    noun = input("Please choose a noun.")
    number = input("Please choose a number.")
    celeb = input("Input a celebrity of your choice.")
    adj = input("Lastly, choose an adjective.")
    madlib = f"{adj} {verb1}  {verb2}  {noun}  {number}  {celeb}"
    print(f"It's a {adj} day outside. As you {verb1} in preparation to {verb2} later in the day, {number} of {noun} stops you! As you start to panic, you look around to see {celeb} watching you from across the street, getting ready to save you. You breathe a sigh of relief, but you come to realize {celeb} does not seem to happy with you.")