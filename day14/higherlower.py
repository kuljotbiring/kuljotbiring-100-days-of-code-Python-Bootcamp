import random
from art import logo as logo
from art import vs as vs
from game_data import data as data


def get_higher(first_result, second_result):
    if first_result[1] > second_result[1]:
        return first_result
    else:
        return second_result


def set_match(dict_list):
    # pick a dictionary at random
    random_dict = random.choice(dict_list)
    # make the values of the dictionary into a list
    list_values = list(random_dict.values())
    return list_values


def display_match(first_pick, second_pick, versus):
    # display the match up
    print(f"Compare A: {first_pick[0]}, a {first_pick[2]}, from {first_pick[3]}")
    print(versus)
    print(f"Compare B: {second_pick[0]}, a {second_pick[2]}, from {second_pick[3]}")


def play_game():
    current_score = 0
    right_answer = []
    go = True
    while go:
        # call function to set up matches. if user correct use previous correct answer as first choice
        if current_score > 0:
            first_result = right_answer
        # other-wise pick a random item
        else:
            first_result = set_match(data)

        # pick a random second item
        second_result = set_match(data)

        # make sure they don't match - if so choose another
        while first_result == second_result:
            second_result = set_match(data)

        # display the match up
        display_match(first_result, second_result, vs)

        # get user selection for which has higher IG follower account
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        right_answer = get_higher(first_result, second_result)

        # set the guess to be the actual number of followers
        if guess == 'a':
            guess = first_result
        else:
            guess = second_result

        # compare guess to answer
        # if correct increase score and display correct message
        if guess == right_answer:
            current_score += 1
            print(f"You're right! Current score: {current_score}")
        # other-wise print finale score and lose message
        else:
            print(f"Sorry, that's wrong. Final score: {current_score}")
            go = False


# show game logo
print(logo)

play_game()



