def factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

number = int(input("Input a number and all of its factors will appear! "))

factors(number)