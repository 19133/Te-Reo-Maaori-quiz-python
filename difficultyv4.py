import time


# user difficulty function
def Chosen_difficulty (question):
  valid=False
  while not valid:
    difficulty_response = input (question) .lower()

    if difficulty_response == "easy" or difficulty_response == "e": 
        difficulty_response = "easy"
        return difficulty_response
        
    elif difficulty_response == "medium" or difficulty_response  == "m":
        difficulty_response = "medium"
        return difficulty_response 

    elif difficulty_response == "hard" or difficulty_response  == "h":
      difficulty_response = "hard"
      return difficulty_response      

  
    elif difficulty_response == "xxx":
      print("Thanks for playing the Te Reo Maaori quiz")
      print("We hope to see you again")
      time.sleep(2)
      exit()   

    else:
      print("Please choose easy, medium or hard") 
      print("Or type xxx to quit") 


# main routine goes here

# asks user if they would like to play on easy, medium, or hard
difficulty = Chosen_difficulty ("What’s red in Te Reo Maaori?\n")

# if easy, the program will print easy difficulty questions
if difficulty == "easy":
  print("you will be playing the quiz on the easy difficulty")
  print()

# if medium, the program will print medium difficulty questions
elif difficulty == "medium":
  print("you will be playing the quiz on the medium difficulty")  

# if hard, the program will print hard difficulty questions
elif difficulty == "hard":
  print("you will be playing the quiz on the hard difficulty")
  print()

elif difficulty == "xxx":
  print ("Thanks for playing the Te Reo Maaori Quiz")
  print ("We hope to see you again")
  time.sleep(2)
  exit()

# else, user is asked to type either easy, madium, or hard. 
else:
  print("Please choose easy, medium, or hard")
  print("Or type xxx to quit")
