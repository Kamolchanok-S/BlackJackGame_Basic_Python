import random

def create_deck():
    """
    Create a standard 52-card deck for Blackjack.

    Returns:
        list: A shuffled list of tuples, each representing a card as (rank, suit, value).
    """
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, '10': 10,
        'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 10
    }
    # create list deck -> tuple (rank, suit, value)
    card_deck = [(rank, suit, value) for suit in suits for rank, value in ranks.items()]
    # shuffe deck
    random.shuffle(card_deck)
    
    return card_deck

def check_blackjack(cards_Player):
    """
    Check if either Player or Dealer has a Blackjack.

    Args:
        scores (dict): Dictionary with keys 'Dealer' and 'Player', values are their scores.

    Returns:
        list: List of winners who have Blackjack.
    """
    winner = []
    if card_draw["Dealer"][1] == 21:
        winner.append("Dealer")
    if card_draw["Player"][1] == 21:
        winner.append("Player")
    return winner
        
def check_winner(winner_list):
    if len(winner_list) > 0:
        print_result(winner_list)
        return True
    return False

def print_result(winner_list):
    """
    Print the result based on the winner list.

    Args:
        winner_list (list): List containing the winner(s), e.g., ['Dealer'], ['Player'], or ['Dealer', 'Player'].
    """
    if len(winner_list) == 2:
        print("No Winner!")
        print("Game tie.")
    elif len(winner_list) == 1:
        print("Found Winner!")
        print(winner_list[0] + " win.")
    else:
        print("No Winner!")
        print("Both bust! There is no winner.")
    print("-----------------------------------------------")
        
def print_cards(cards_Player, round):
    """
    Print cards in a readable format.

    Args:
        cards_Player (dict): A dict of list of card tuples.
    """
    print(f"Round: {round}\n")
    print("Dealer's cards:")
    for i, (rank, suit, _) in enumerate(cards_Player['Dealer'][0]):
        print(f"{rank} of {suit}")
    print(f"Dealer total: {cards_Player['Dealer'][1]}")

    print("\nPlayer's cards:")
    for i, (rank, suit, _) in enumerate(cards_Player['Player'][0]):
        print(f"{rank} of {suit}")
    print(f"Player total: {cards_Player['Player'][1]}")
    print("-----------------------------------------------")

def draw_card(cards_Player, person, card_deck):
    """
    Draw a card from the deck and update the Player's or Dealer's hand and total value.

    Args:
        cards_Player (dict): Dictionary holding hands and totals for 'Player' and 'Dealer'.
        person (str): Either 'Player' or 'Dealer'.
        card_deck (list): The current deck of cards to draw from.
    """
    new_card = card_deck.pop()
    cards_Player[person][0].append(new_card)
    cards_Player[person][1] += new_card[2]

def check_bust(card_Player):
    """
    Check if either the Dealer or the Player has busted (score > 21).
    
    Args:
        card_Player (dict): Dictionary with 'Dealer' and 'Player' as keys, each mapping to [hand, total].
    
    Returns:
        bool: True if a bust occurs, otherwise False.
    """
    Dealer_total = card_Player["Dealer"][1]
    Player_total = card_Player["Player"][1]
    
    if Dealer_total > 21 and Player_total > 21:
        print_result(["Dealer", "Player"])
        return True
    elif Dealer_total > 21:
        print_result(["Player"])
        return True
    elif Player_total > 21:
        print_result(["Dealer"])
        return True
    return False
    
def Dealer_turn(card_draw, deck):
    """
    Dealer draws cards until reaching 17 or higher.

    Args:
        card_draw (dict): Dictionary with Dealer's cards and total.
        deck (list): The current shuffled deck of cards.
    """
    while card_draw["Dealer"][1] < 17:
        draw_card(card_draw, "Dealer", deck)

def check_highNumber(cards_Player):
    """
    Compare final hand values and determine the winner.

    Args:
        cards_Player (dict): Dictionary with 'Dealer' and 'Player' hands and totals.

    Returns:
        list: A list containing the winner(s). Can be ['Player'], ['Dealer'], or ['Dealer', 'Player'] for a tie.
    """
    Player_total = cards_Player["Player"][1]
    Dealer_total = cards_Player["Dealer"][1]

    if Player_total > Dealer_total:
        return ["Player"]
    elif Dealer_total > Player_total:
        return ["Dealer"]
    else:
        return ["Dealer", "Player"]  # Tie 

game_run = True

while game_run:
    # Start Game
    deck = create_deck()

    # Initialize card_draw dictionary
    card_draw = {
        "Dealer": [[], 0],
        "Player": [[], 0]
    } #value = [[card1, card2], total value]

    count_round = 1
    # Deal 2 cards each
    for role in ["Dealer", "Player"]:
        hand = [deck.pop(), deck.pop()]
        total = sum(card[2] for card in hand)
        card_draw[role] = [hand, total]

    print_cards(card_draw, count_round)
    game_stop = check_blackjack(card_draw)
    game_stop = check_bust(card_draw)

    # Dealer hit until >= 17
    Dealer_turn(card_draw, deck)
    print("Dealer card for next round: ")
    print_cards(card_draw, count_round + 1)
    game_stop = check_bust(card_draw)

    # all rounds
    while not game_stop:
        count_round += 1
        if input("Player would you like to hit? (Y/N): ")[0].upper() == 'Y':
            draw_card(card_draw, "Player", deck)
            print_cards(card_draw, count_round)
            game_stop = check_bust(card_draw)
        else: # game end -> find winner
            winner = check_highNumber(card_draw)
            game_stop = check_winner(winner)
            
    print("GAME FINISH.")
    game_run = True if input("Would you like to play another round? (Y/N)").upper() == 'Y' else False
