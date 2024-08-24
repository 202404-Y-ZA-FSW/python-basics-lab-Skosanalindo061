import random

def number_guessing_game():


  
  secret_number = random.randint(1, 100)


  attempts = 0

  print("hello this is Lindokuhle Number Guessing Game! my friends call me (LNGG)")
  print("i have a number between 1 and 100. i want you to guess it.")


  while True:
    try:
      
      guess = int(input("Lindokuhle says Take a guess: "))
      attempts += 1

      
      if guess == secret_number:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
      elif guess < secret_number:
        print("Too low Try again.")
      else:
        print("Too high Try again.")
    except ValueError:
      print("opps Lindokuhle says Invalid input  Please enter a number.")


number_guessing_game()
