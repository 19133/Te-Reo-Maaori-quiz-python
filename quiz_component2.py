score = 0

# red question function
def quiz_question(question):
  valid=False
  while not valid:
    user_response = input (question) .lower()

    if user_response == "whero":
        user_response = "whero"
        return user_response 

    else:
      print("Incorrect, try again") 

# ocean question function
def quiz_question2(question):
  valid=False
  while not valid:
    user_response = input (question) .lower()

    if user_response == "moana":
        user_response = "moana"
        return user_response 

    else:
      print("Incorrect, try again") 


# main routine goes here

# whats red in te reo maaori? question componenet
qna_whero = quiz_question ("What’s red in Te Reo Maaori?\n")

if qna_whero == "whero":
  print("Correct")
  score += 1
  print()

else:
  print("Incorect, try again")
  print()

# whats ocean in te reo maaori? question componenet
qna_awa = quiz_question2 ("What’s ocean in Te Reo Maaori?\n")

if qna_awa == "moana":
  print("Correct")
  score += 1
  print()

else:
  print("Incorect, try again")
  print()
