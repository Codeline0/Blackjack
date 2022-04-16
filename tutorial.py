def main(name):
    print('''
The main objective in Blackjack is that each participant attempts to beat the dealer by getting a count 
as close to 21 as possible, without going over 21, pretty simple right?
There are 52 cards in 1 deck, and we'll be playing with 6 decks.

Each deck has 4 sections:

◆, ♥, ♠ and ♣

And each section has this cards:

Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K

Cards are valued:
______________________
|J/Q/K  |  10        |
|Ace    |  1 or 11   |
|2-10   |  Face Value|
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Before the deal begins, each player places a bet.
When all the players have placed their bets, the dealer gives one card face up to each player and then one card face up to themselves. 
Another round of cards is then dealt face up to each player, but the dealer takes the second card face down. 
Thus, each player except the dealer receives two cards face up, and the dealer receives one card face up and one card face down.
Obviously, this is a text game, so the "cards" are just letters and numbers.

This is still the overiew. Let's start with a simple game, and I'll walk you through it, shall we? y/n
    ''')

    answer = input()
    #Loops until the answer is y, it would've repeated the instructions, but it would just be a wall of repeating text at that point
    while answer != "y":
        print("What? Was it not clear? I'm going to ask again, shall we start? y/n")
        answer = input()
    print("\033c")
    print('''

    '''.format(name = name))

if __name__ == "__main__":
    main()