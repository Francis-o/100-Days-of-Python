"""
Blackjack game
"""

import random
import blackjack_art

#create function that compares player and computer cards
def compare_cards(user_cards,  computer_cards):
    sum_user_cards = sum(user_cards)
    sum_computer_cards = sum(computer_cards)
    if sum_user_cards > 21 and 11 in user_cards:
        user_cards[user_cards.index(11)] = 1
        return {"game_end": False, "game_status": "replaced ace for user"}
    elif sum_computer_cards > 21 and 11 in computer_cards:
        computer_cards[computer_cards.index(11)] = 1
        return {"game_end": False, "game_status": "replaced ace for computer"}
    elif sum_user_cards == 21 and sum_computer_cards != 21 and len(user_cards) == 2:
        return {"game_end": True, "game_status": "Win😃", "game_message": "You have blackjack"}
    elif sum_computer_cards == 21 and sum_user_cards != 21 and len(computer_cards) == 2:
        return {"game_end": True, "game_status": "Lose😭", "game_message": "Computer has blackjack"}
    elif sum_user_cards == sum_computer_cards:
        return {"game_end": False, "game_status": "Draw", "game_message": "You have the same card"}
    elif sum_user_cards > 21:
        return {"game_end": True, "game_status": "Lose😭", "game_message": "You went over"}
    elif sum_computer_cards > 21:
        return {"game_end": True, "game_status": "Win😃", "game_message": "Computer went over"}
    elif sum_user_cards > sum_computer_cards:
        return {"game_end": False, "game_status": "Win😃", "game_message": "You have higher cards"}
    elif sum_computer_cards > sum_user_cards:
        return {"game_end": False, "game_status": "Lose😭", "game_message": "Computer has higher cards"}

def blackjack():
    print(blackjack_art.logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    #use a function to append two cards each for computer and user and make sure it doesn't remove the cards on selection
    user_cards = random.choices(cards, k=2)
    computer_cards = random.choices(cards, k=2)
    end_of_game = False
    while not end_of_game:
        game_data = compare_cards(user_cards=user_cards, computer_cards=computer_cards)
        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")
        if game_data["game_end"] == False:
            add_card = input(f"Type 'y' to get another card. type 'n' to pass: ").lower()
            if add_card == 'y':
                user_cards.append(random.choice(cards))
                game_data = compare_cards(user_cards=user_cards, computer_cards=computer_cards)
                if (sum(computer_cards) < 17 or sum(computer_cards) < 21) and len(user_cards) >= 3 and game_data["game_end"] == False:
                    computer_cards.append(random.choice(cards))
            elif add_card  == "n":
                game_data = compare_cards(user_cards=user_cards, computer_cards= computer_cards)
                end_of_game = True
        else:
            end_of_game = True
    print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
    print(f"{game_data["game_message"]}. You {game_data["game_status"]}")

end_loop = False
while not end_loop:
    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if start_game == 'y':
        blackjack()
        print("\n" * 20)
    else:
        end_loop = True
