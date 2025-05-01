# BlackJackGame_Basic_Python
🃏 Blackjack Console Game in Python
- This is a simple text-based Blackjack game implemented in Python. The game simulates a classic round of Blackjack between a player and a dealer using a 52-card deck. It is a great project to understand object manipulation, functions, conditional logic, and user input in Python.

🎮 Game Features
- Uses a shuffled 52-card deck (no jokers)
- Supports dealer logic: hits until the hand total reaches at least 17
- Detects blackjack and bust conditions
- Compares scores to determine the winner
- Offers multiple rounds based on user input

🛠 How It Works
- The deck is created with 52 cards, represented as (rank, suit, value) tuples.
- Each round:
    - Both Dealer and Player receive 2 cards.
    - The game checks for immediate Blackjacks or busts.
    - The dealer automatically hits until the score is 17 or more.
    - The player chooses whether to hit or stand.
    - If no one busts, scores are compared to determine the winner.
- After each round, you are prompted to play again.

📌 Notes
- Face cards (Jack, Queen, King) are worth 10.
- Aces are currently fixed at 10 (not 1 or 11).
- Basic error handling is included for user inputs.
- Designed for educational and practice purposes.
