#Number Guessing Game:


from random import randint

#global constant
EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5


#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """Check answer agains guess return the number of turns remaining"""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

# Make function to sset difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURN
  else:
    return HARD_LEVEL_TURN

def game():   
# Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Psst, the correct answer is {answer}")
  
  #Make function to set difficulty.
  turns = set_difficulty()
  print(f"You have {turns} attemps reaming to guess the number.")
  
  # Repeat the guessing functionality if they get it wrong.
  guess = 0 
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
  
    #Let the user guess a number.
    guess = int(input("Make a guess:"))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again")
game()
