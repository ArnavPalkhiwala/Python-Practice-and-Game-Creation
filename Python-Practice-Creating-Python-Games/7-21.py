# # counter = 0

# # while counter <= 20:
# #   print(f'The counter is now {counter}')
# #   counter += 1

# for x in range(10):
#   print(x)

import random

# print(random.randint(0,100))
#Guessing Game

# guess = 0
# number = random.randint(0,1000)

# while guess != number:
#   guess = int(input("Guess a number between 0 and 100...\n"))
#   if guess < number:
#     print("Too low, guess again!")
#   elif guess == number:
#     print("Congrats, you guessed it!")
#     break
#   else:
#     print("Too high, try again!")

##Favorite Food Guessing Game

#def favoriteFood():
#   guesses = random.randint(0,10)
#   while guesses > 0:
#     food = input("What do you think my favorite food is\n").lower()
#     if food == "pizza":
#       print("You got it!")
#       break
#     else:
#       print("Try again!")
#       guesses -= 1
#   if guesses == 0:
#     print("You are out of guesses")

# favoriteFood()

class MyPet:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def play_fetch(self):
    print("Your pet " + pet.name + " is having fun playing fetch!")

pet = MyPet("None", 199)

print(pet.name)
print(pet.age)
     
pet.play_fetch()