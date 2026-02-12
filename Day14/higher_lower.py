"""
higher lower game
"""

#import data 
import random
import higher_lower_data
import higher_lower_art


def update_score(score):
    """
    returns addition of one to score
    """
    return score + 1

def compare_choice(data, pick_one, score):
    """
    This returns the data of the winner, game status and updated score
    
    :data: This is a list of all the items to compare with
    :param pick_one: This is the first item gotten from the list to compare with
    :param score: user sccore
    """
    pick_two = random.sample(data, k=1)[0]
    print(f"Compare A: {pick_one["name"]}, {pick_one["description"]}, from {pick_one["country"]}.")
    print(higher_lower_art.VS)
    print(f"Against B: {pick_two["name"]}, {pick_two["description"]}, from {pick_two["country"]}.")
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    if choice == "A" and (pick_one["follower_count"] > pick_two["follower_count"]):
            return {"win_value": pick_one, "new_score": update_score(score), "game_end": False}
    elif choice == "B" and (pick_two["follower_count"] > pick_one["follower_count"]):
            return {"win_value": pick_two, "new_score": update_score(score), "game_end": False}
    else:
         return {"game_end": True}
    

def higher_lower():
    print(higher_lower_art.GAME_ART)
    data = higher_lower_data.data
    first_pick = random.sample(data, k=1)[0]
    score = 0
    end_of_game = False

    while not end_of_game:
        if len(data) == 0:
             print(f"GAME OVER! Final score: {score}")
             return
        result = compare_choice(data=data, pick_one=first_pick, score=score)
        if result["game_end"]  == False:
            score = result["new_score"]
            print(f"You're right! Current score: {score}.")
            first_pick = result["win_value"]
        elif result["game_end"] == True:
             print(f"Sorry, that's wrong. Final score: {score}")
             end_of_game = result["game_end"]

higher_lower()