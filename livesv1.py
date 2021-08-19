play_lives = input ("Would you like to play with lives\n")

# if yes, the user will be asked how many lives would they like to have
if play_lives == "yes":
  print ("Thats great")
  print("How many lives would you like to play with")
  user_lives = int(input()) 
  print("You will be playing with {} lives".format(user_lives))


else:
  print("You will be playing with 0 lives")
  user_lives = 0
