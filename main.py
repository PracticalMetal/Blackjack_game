import random
import os
os.system('cls' if os.name == 'nt' else 'clear')
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
from art import logo

def choice_no(current_computer_sum,current_user_sum,computer_card,user_card):
        while current_computer_sum<17:
            computer_card.append(random.choice(cards))
            current_computer_sum+=computer_card[i]
        print(f"Your final hand: {user_card}, final score: {current_user_sum}")
        print(f"Computer's final hand: {computer_card}, final score: {current_computer_sum}")

        if current_computer_sum>21:
            print("Opponent went over, You Win! 😁")
        elif current_user_sum>current_computer_sum:
            print("You have higher score, You Win! 😁")
        elif current_computer_sum==current_user_sum:
            print("Push!")
        else:
            print("Opponent has higher score, Better luck next time!")
        continue_game=input("Do you want to play again? type 'y' or 'n': ").lower()
        os.system('clear')

def choice_yes(current_computer_sum,current_user_sum,computer_card,user_card):
    new_card=random.choice(cards)
    if new_card==11 and current_user_sum+new_card>21:
        new_card=1
    user_card.append(new_card)
    current_user_sum+=new_card
    if current_user_sum>21:
        print("You went over, Better luck next time!")
    else:
        print(f"Your cards: {user_card}, current score is: {current_user_sum}")
        print(f"Computer's first card is: {computer_card[0]}")
        wish_to_continue=input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if wish_to_continue=='y':
            choice_yes(current_computer_sum,current_user_sum,computer_card,user_card)      
        else:
            choice_no(current_computer_sum,current_user_sum,computer_card,user_card)

continue_game=input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()



while continue_game=='y':
    user_card=[]
    computer_card=[]
    current_user_sum=0
    current_computer_sum=0
    print(logo)
    for i in range(0,2):
        user_card.append(random.choice(cards))
        current_user_sum+=user_card[i]
        computer_card.append(random.choice(cards))
        current_computer_sum+=computer_card[i]
    print(f"Your cards: {user_card}, current score is: {current_user_sum}")
    print(f"Computer's first card is: {computer_card[0]}")
    deal_or_pass=input("Type 'y' to get another card, type 'n' to pass: ").lower()

    if deal_or_pass=='n':
        # def choice_no():
        while current_computer_sum<17:
            computer_card.append(random.choice(cards))
            current_computer_sum+=computer_card[i]
        print(f"Your final hand: {user_card}, final score: {current_user_sum}")
        print(f"Computer's final hand: {computer_card}, final score: {current_computer_sum}")

        if current_computer_sum>21:
            print("Opponent went over, You Win! 😁")
        elif current_user_sum>current_computer_sum:
            print("You have higher score, You Win! 😁")
        elif current_computer_sum==current_user_sum:
            print("Push!")
        else:
            print("Opponent has higher score, Better luck next time!")
        continue_game=input("Do you want to play again? type 'y' or 'n': ").lower()
        os.system('clear')
        
    
    else:
        #def choice_yes():
        new_card=random.choice(cards)
        if new_card==11 and current_user_sum+new_card>21:
            new_card=1
        user_card.append(new_card)
        current_user_sum+=new_card
        if current_user_sum>21:
            print(f"Your cards: {user_card}, current score is: {current_user_sum}")
            print("You went over, Better luck next time!")
            continue_game=input("Do you want to play again? type 'y' or 'n': ").lower()
            os.system('clear')
            
        else:
            print(f"Your cards: {user_card}, current score is: {current_user_sum}")
            print(f"Computer's first card is: {computer_card[0]}")
            wish_to_continue=input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if wish_to_continue=='y':
                choice_yes(current_computer_sum,current_user_sum,computer_card,user_card)
            else:
                choice_no(current_computer_sum,current_user_sum,computer_card,user_card)
    