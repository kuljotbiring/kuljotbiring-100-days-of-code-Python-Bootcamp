import art
import random

# ############## Blackjack Project #####################

# ############## Our Blackjack House Rules #####################

# # The deck is unlimited in size.
# # There are no jokers.
# # The Jack/Queen/King all count as 10.
# # The  Ace can count as 11 or 1.
# # Use the following list as the deck of cards:
# # cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# # The cards in the list have equal probability of being drawn.
# # Cards are not removed from the deck as they are drawn.
# # The computer is the dealer.


# prints the blackjack logo
def logo():
    print(art.logo)


def score(user_deck, computer_deck, go_again):
    player_score = sum(user_deck)
    dealer_score = sum(computer_deck)

    if go_again == "y":
        if player_score > 21:
            print("You went over. You lose!")
            return False
    else:
        print(f"Your final hand: {user_deck}, current score: {sum(user_deck)}")
        print(f"Dealer's final hand: {computer_deck}, current score: {sum(computer_deck)}")

        if player_score == dealer_score:
            print("Tie game! It's a draw!")
        elif player_score > 21:
            print("You went over. You lose!")
        elif dealer_score > 21:
            print("Dealer went over. You win!")
        elif player_score > dealer_score:
            print("You win")
        else:
            print("You lose")
        return False

    return True


# adds a random card to the chosen deck
def add_card(deck, player_deck):
    # grab a new card from the deck
    new_card = random.choice(deck)
    # if new card is an Ace and adding it to player pile makes
    # sum go over 21, Ace can be changed to a 1
    if new_card == 11:
        if (new_card + sum(player_deck)) > 21:
            print("Ace drawn and changed to a '1'")
            new_card = 1
    # add new card to the player's deck
    player_deck.append(new_card)


# creates deck of cards and give dealer and player two cards
def new_deal():
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_deck = []
    dealer_deck = []
    add_card(deck, player_deck)
    add_card(deck, player_deck)
    add_card(deck, dealer_deck)
    add_card(deck, dealer_deck)

    # show first user cards drawn and dealer first card
    print(f"Your cards: {player_deck}, current score: {sum(player_deck)}")
    print(f"Dealer's first card: {dealer_deck[0]}")

    return deck, player_deck, dealer_deck


# function checks if user wants to restart game
def start_game():
    go_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    return go_again


def blackjack():
    # call function to create a new deck and unpack return tuple in variables
    deck, player_deck, dealer_deck = new_deal()

    play_game = True
    while play_game:
        # check if player lost
        if not score(player_deck, dealer_deck, "y"):
            break
        # ask user if they want another card
        draw_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if draw_card == "y":
            # add a card to the player's deck
            add_card(deck, player_deck)
            print(f"Your cards: {player_deck}, current score: {sum(player_deck)}")
            print(f"Dealer's first card: {dealer_deck[0]}")
            continue
        elif draw_card == "n":
            # dealer must draw if current total is less than 17
            while sum(dealer_deck) < 17:
                add_card(deck, dealer_deck)
            # check the dealer's score
            score(player_deck, dealer_deck, "n")
            break


# display logo
logo()

play = True

while play:

    run_game = start_game()
    # check if user wants to play
    if run_game == "n":
        play = False
    elif run_game == "y":
        # call game function
        blackjack()



