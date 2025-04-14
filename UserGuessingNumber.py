import random

def computerguess(x):
   anynumber= random.randint(1,x)
   computerguess=0
   while computerguess!= anynumber:
       computerguess=int(input(f"Guess any number between 1 and {x}:   "))
       if computerguess<anynumber:
           print("Oops!The number is too low. Try again.")
       elif computerguess>anynumber:
           print("Oopas! The numberis too high. Try again.")
       
   print(f'Congratulations! You have guessed the right number{anynumber}')

computerguess(20)