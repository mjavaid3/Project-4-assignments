# program to let the AI guess the secret number in your mind
import random 

def mind_reader(max_num):
    minimum_range = 1
    maximum_range = max_num
    player_response = ""
    
    while player_response != "c":
        if minimum_range != maximum_range:
            ai_prediction = random.randint(minimum_range, maximum_range)
        else:
            ai_prediction = minimum_range
            
        player_response = input(f"Is {ai_prediction} too big (h), too small (l) or correct (c)? ")
        
        if player_response == "h":
            maximum_range = ai_prediction - 1 
        elif player_response == "l":
            minimum_range = ai_prediction + 1
            
    print(f"Amazing! The AI has read your mind and found the correct number: {ai_prediction}.")

mind_reader(20)
