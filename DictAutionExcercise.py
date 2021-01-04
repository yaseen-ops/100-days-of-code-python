import art

print(art.dictionary_logo)

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The Winner is {winner} with a bid of {highest_bid} ")


while not bidding_finished:
    name = input("Enter your name : ")
    price = int(input("Enter your bidding price : $"))
    bids[name] = price
    should_continue = input("Are there any bidders? Type 'yes' or 'no' \n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
        print("\n")
# print(bidding_dit)
