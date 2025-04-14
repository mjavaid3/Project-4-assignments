# program to let the computer guess the number user is thinking
import random 
def userguess(x):
    low = 1
    high = x
    userfeedback = ""
    while userfeedback != "c":
        if low != high :
            guess = random.randint(low, high)
        else:
            guess= low
        userfeedback = input(f"Is {guess} too high (h), too low(l) or correct(c)")
        if userfeedback=="h":
            high = guess-1 
        elif userfeedback=="l":
            low = guess+1
    print(f"Yeah! The computer has guessed the right number {guess}.")
userguess(20)