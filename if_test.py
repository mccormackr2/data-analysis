name = input("what is your name?")
my_number = 0

while (my_number < 100):
 my_number = input("Hello " +name +" please pick a number bigger than 100")
 my_number = int(my_number)
 print("Your number is " +str(my_number))

 if (my_number >= 100):
  print("that's a big number")
 elif (my_number > 90 and my_number < 100):
  print("almost there, try again")
 else:
  print("that number is too small, please try again")
