import art


def enter_bid(dict):
    # get input from user
    name = input("What is your name?: ")
    amount = int(input("What is your bid?: "))

    # fill key values
    dict[name] = amount


def check_winner(dictionary):
    top_bidder = ""
    highest_bid = 0
    # run through dictionary keys and check value with the highest dollar
    for key in dictionary:
        if dictionary[key] > highest_bid:
            # update the name and amount of highest bidder
            top_bidder = key
            highest_bid = dictionary[key]
    # display the highest bidder
    print(f"The winner is {top_bidder} with a bid of ${highest_bid}")
print(art.logo)
print("Welcome to the secret auction program.")
# create empty dictionary to hold bidders and amounts
bidders = {}

run_auction = True
# keep program going while there are more people in auction
while run_auction:
    # call function to add to dictionary
    enter_bid(bidders)
    # check if more names to be entered - otherwise exit
    more_bids = input("Are there any other bidders? Type 'yes' or 'no. ").lower()
    if more_bids == 'no':
        run_auction = False

# check for the winner
check_winner(bidders)
