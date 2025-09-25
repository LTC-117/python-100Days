import art
import random


deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
result: int = 0


def draw_card(amount, list = []):
    for i in range(amount):
        list.append(random.choice(deck))


def calculate_score(list = []):
    result: int = 0

    for i in list:
        result += i

    return result


def end_game(player, computer, player_score):
    while calculate_score(computer) < 21:
        draw_card(1, computer)

    computer_score = calculate_score(computer)

    total_dif = player_score - computer_score

    print(f"Your final hand: {player}, final score: {player_score}")
    print(f"Computer's final hand: {computer}, final score: {computer_score}")

    if computer_score > 21:
        print("Opponent went over!!!")
        return 1

    return total_dif


def blackjack(player, computer, player_amount):
    blackjack_result: int = 0
    draw_card(1, computer)

    draw_card(player_amount, player)

    player_score = calculate_score(player)

    print(f"Your cards: {player}, current score: {player_score}")
    print(f"Computer's first card: {computer[0]}")

    if player_score == 21:
        print("Blackjack!!!")
        return 1
    elif player_score > 21:
        print("You went over!!!")
        return -1

    hit_or_stand = input("Type 'y' to get another card, type 'n' to pass: ")

    if hit_or_stand == 'y':
        blackjack(player, computer, 1)
    else:
        blackjack_result = end_game(player, computer, player_score)

    return blackjack_result


while result == 0:
    user_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if user_input == 'n':
        exit(0)

    print(art.logo)

    player_cards = []
    computer_cards = []

    result = blackjack(player_cards, computer_cards, 2)

    if result > 0:
        print("You win!!! 😃")
        exit(0)
    elif result == 0:
        print("Draw!!!")
        exit(0)
    else:
        print("You lose!!! 😭")
        exit(0)

