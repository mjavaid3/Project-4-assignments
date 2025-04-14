import random

def number_hunter(upper_limit):
    secret_number = random.randint(1, upper_limit)
    player_attempt = 0
    
    while player_attempt != secret_number:
        player_attempt = int(input(f"🔍 Find the hidden number between 1 and {upper_limit}: "))
        
        if player_attempt < secret_number:
            print("⬆️ Too low! Aim higher, adventurer!")
        elif player_attempt > secret_number:
            print("⬇️ Too high! Come down a bit!")
    
    print(f'🎉 Victory! You\'ve uncovered the secret number {secret_number}!')

number_hunter(20)
