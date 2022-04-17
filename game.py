import random
import text_effects

class Player:
    cards_in_hand = []
    sum_of_cards = 0
    money = 100
    bet = 0
    blackjack = False
    pairs = False
    bust = False
    ace = False
    hit = False
    stand = False
    double_down = False
    game_over = False

    def __init__(self, name, is_dealer=False):
        self.name = name
        self.is_dealer = is_dealer
    
    def dealer_money(self):
        if self.is_dealer == True:
            self.money += 10000000

    def bet_money(self, num):
        if num <= self.money:
            self.money -= num
            self.bet += num
        else:
            return False
    
    def lost(self):
        self.bet -= self.bet

    def win(self):
        if self.double_down == True:
            self.bet += self.bet*2
        else:
            self.bet += self.bet
    
    def busted(self):
        self.bust = True

    def pair(self):
        self.pairs = True
    
    def has_ace(self):
        self.ace = True
    
    def sum_cards_hand(self):
        non_nums = {
        "J" : 10,
        "Q" : 10,
        "K" : 10,
        "A" : [1, 11]
    }
        for card in self.cards_in_hand:
            value = card[:1]
            
            


def create_decks(num_decks = 6):
    decks = []
    symbols = ["♠", "♥", "◆", "♣"]
    letter_sym = ["J", "Q", "K", "A"]
    count = 0

    while count < num_decks:
        for symbol in symbols:
            for num in range(2, 11):
                card = symbol + str(num)
                decks.append(card)

            for letter in letter_sym:
                card = symbol + letter
                decks.append(card)
        count += 1
    return decks

def deck_shuffle(deck):
    random.shuffle(deck)
    return deck

def betting(player, num):
    allowed = [5, 10, 15, 20]

    if num in allowed:
        if player.bet_money(num) == False:
            text_effects.writing_effect("Not enough funds! You have ${} remaining! Pick 5, 10, 15 or 20:\n".format(player.money))
            num = input()
            betting(player, num)
        else:
            player.bet_money(num)
    else:
        text_effects.writing_effect("Nope, pick between 5, 10, 15 or 20:\n")
        num = input()
        betting(player, num)
        
def dealing(shuffled_deck, card_pile, lst_players):
    for player in lst_players:
        for i in range(2):
            card = shuffled_deck.pop()
            card_pile.append(card)
            player.cards_in_hand.append(card)

def return_pile(card_pile, used_deck):
    for card in card_pile:
        used_deck.append(card)
    return used_deck

def player_turn()
