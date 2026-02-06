"""
Secret Auction
"""
import secret_auction_art

print(secret_auction_art.banner)
bidders = {}
def highest_bidder(bidder_dict):
    highest_score = 0
    highest_bidder = ""        
    for key in bidder_dict:
        if bidders[key] > highest_score:
            highest_score = bidders[key]
            highest_bidder = key
    print(f"The winner is {highest_bidder.capitalize()} with a bid of ${highest_score}")

end_of_auction = False
while not end_of_auction:
    name = input("What is your name?: ")
    bid_amount = int(input("What is your bid?: "))
    bidders[name] = bid_amount
    next_bidder = input("Are there any other bidders? Type 'yes' or 'no'")
    if next_bidder == "yes":
        print("\n"*100)
    elif next_bidder == "no":
        highest_bidder(bidder_dict=bidders)
        end_of_auction = True

    