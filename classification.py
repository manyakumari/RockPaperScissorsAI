import cv2 as cv
from cvzone import ClassificationModule
import random as r

cap = cv.VideoCapture(0)
gesture = ClassificationModule.Classifier("rock_paper_scissors/keras_model.h5","rock_paper_scissors/labels.txt")
print("WELCOME TO ROCK PAPER SCISSORS! Make the gesture you want to play and play against the computer!")
Player_score = 0
Computer_Score = 0
print("Type s to see score and end game, else type c to continue")
seescore = input()

while seescore == "c":
    ret,frame = cap.read()
    prediction = gesture.getPrediction(frame)
    value= prediction[-1]
    
    signs = ["rock", "paper", "scissors"]
    computer_sign = r.choice(signs)
    print("Computer chose ", computer_sign, "!")

    if value == 0:
       print ("You chose Rock!")
       cv.circle(frame, (350,350), 100,(255,0,0))
    elif value == 1:
        print("You chose Paper!")
        cv.rectangle(frame, (350,350), (400,300), (0,255,0), 7)
    elif value ==2:
        print("You chose Scissors!")
        cv.putText(frame, "SCISSORS", (350,350), cv.FONT_HERSHEY_COMPLEX, 10, (0,0,255), 7)

    if computer_sign == "rock" and value == 0:
        print("Its a tie!")
    elif computer_sign == "rock" and value == 1:
        print("You win!")
        Player_score +=1
    elif computer_sign == "rock" and value == 2:
        print("Computer wins!")
        Computer_Score +=1


    elif computer_sign == "paper" and value == 0:
        print("Computer wins!")
        Computer_Score +=1
    elif computer_sign == "paper" and value == 1:
        print("Its a tie!")
    elif computer_sign == "paper" and value == 2:
        print("You win!")
        Player_score +=1


    elif computer_sign == "scissors" and value == 0:
        print("You win!")
        Player_score +=1
    elif computer_sign == "scissors" and value == 1:
        print("Computer wins!")
        Computer_Score +=1
    elif computer_sign == "scissors" and value == 2:
        print("Its a tie!")
    
    print("Type s to see score and end game, else type c to continue")
    seescore = input()
    cv.imshow("vid",frame)
    key=cv.waitKey(10)
    if key == 27:
        break

print("Computer final score: ", Computer_Score)
print("Your final score:", Player_score)
if Computer_Score > Player_score:
    print("Computer won overall! Better luck next time!")
elif Computer_Score == Player_score:
    print("Oooh it's a tie!")
else:
    print("Yay you won!!")

