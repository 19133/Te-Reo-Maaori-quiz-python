import random


# quiz questions 
Questions_answers = {
    "What is ocean in Te Reo Maaori? \n A. kātao\n B. Moana\n C. Awa \n D. Wai":"b",
    "What is red in Te Reo Maaori?  \n A. whero \n B. Red \n C. whrea \n D. rato" :"a",
    "If it is Ua it is what? \n A. Rainy \n B. Sunny \n C. hot \n D. 21 hours ":"a"
}   

score = 0
question = list (Questions_answers.keys())
#input answer here 
while True:
    if not question:
        break
    ques = random.choice(question)
    print(ques)
    while True:
        answer = input('Answer ' )
        # if correct, moves onto next question
        if answer.lower() == Questions_answers[ques]:
            print("Correct Answer")
            print ()
            # if correct, score goes up by 1
            score + 1
            print("total score is", score)
            print()
            break
        else:
            #if wrong, Asks the same question again
            print("Wrong Answer, try again")
            score -= 1
            if score < 1:
              score = 0
            print ("Your score is now", score)
    question.remove(ques)