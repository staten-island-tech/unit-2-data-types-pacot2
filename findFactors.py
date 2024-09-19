factorStorage = []
def callFactors(x):
   print(f"The factors of {number} are:")
   for i in range(1, x + 1):
       if x % i == 0:
           factorStorage.append(i)

number = int(input("Input a number and all of its factors will appear! "))
print("Disclaimer: Inputting a number that has more than 10 digits (for whatever godforsaken reason) will take a long time to load! Please don't be annoying")

callFactors(number)
print(factorStorage)