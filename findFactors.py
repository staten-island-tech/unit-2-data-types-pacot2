factorStorage = []
def callFactors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           factorStorage.append(i)

number = int(input("Input a number and all of its factors will appear! "))

callFactors(number)
print(factorStorage)