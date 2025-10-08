import art
import game_data
import random
import os


def compare_results(user_choice, other_option):
    return user_choice - other_option


def end_game(final_score):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {final_score}")
    exit()


def higher_lower(user_score, element_a = {}, element_b = {}):
    result = 0

    print(f"Compare A: {element_a['name']}, a {element_a['description']}, from {element_a['country']}")
    print(art.vs)
    print(f"Against B: {element_b['name']}, a {element_b['description']}, from {element_b['country']}")
    user_input = input("Who has more followers? Type 'A' or 'B': ").upper()

    match user_input:
        case 'A':
            result = compare_results(element_a['follower_count'], element_b['follower_count'])
        case 'B':
            result = compare_results(element_b['follower_count'], element_a['follower_count'])
        case _:
            end_game(user_score)

    if result >= 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        user_score += 1
        print(art.logo)
        print(f"You're right! Current score: {user_score}")
        higher_lower(user_score, element_b, random.choice(game_data.data))
    else:
        end_game(user_score)


while 1:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(art.logo)
    higher_lower(0, random.choice(game_data.data), random.choice(game_data.data))
