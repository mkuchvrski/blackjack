import random
from art import logo

def get_card(user_cards):
    user_cards.append(random.choice(cards))


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

game_status = True
computer_cards = []
player_cards = []
get_card(player_cards)
get_card(computer_cards)

def blackjack():
    get_card(player_cards)
    get_card(computer_cards)
    player_score = sum(player_cards)
    computer_score = sum(computer_cards)
    print(f"    Your cards: {player_cards}, current score {player_score}.")
    print(f"    Computer's cards: {computer_cards[:-1]}.")
    if player_score > 21:
        print(f"You went over! You lose!")
    else:
        should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
        if should_continue == 'y':
            blackjack()
        else:
            if (computer_score < player_score) or (computer_score > 21):
                print(f"Computer final hand: {computer_cards}, final score: {computer_score}.")
                print(f"You win!")
            elif computer_score == player_score:
                print(f"Computer final hand: {computer_cards}, final score: {computer_score}.")
                print(f"Draw!")
            else:
                print(f"Computer final hand: {computer_cards}, final score: {computer_score}.")
                print(f"You lose!")


play_blackjack = input("Do you want to play blackjack? Type 'y' or 'n'. ")
if play_blackjack == "y":
    blackjack()
