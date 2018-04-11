name = input("what is your name?")
guess = 0
ray_number = 6
counter_number = 0

while (counter_number < 5 and guess != ray_number):
 counter_number = counter_number + 1
 my_number = input("Hello " +name +" Lets play a game, you have 5 gueses to pick my number between 1 and 9")
 guess = int(guess)
 print("Your number is " +str(guess))
  
 if (guess == ray_number):
  print("congrats, you picked the correct number")
 elif (guess > ray_number):
  print("close but you guessed too high, retry")
 elif (guess < ray_number):
  print("close but you guessed too low, retry")
 else:
  print("close but incorrect, please try again")

 if (counter_number == 5):
  print("sorry but you maxed out your 5 allowed guesses")
