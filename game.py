import random
from xml.dom import ValidationErr
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
            self.money += self.bet*2
            text_effects.writing_effect("Congratulations! You won ${}!".format(self.bet))
            self.bet = 0
        elif self.blackjack == True:
            self.money += self.bet * 2.5
            text_effects.writing_effect("BLACKJACK!!! Congratulations! You won ${}!".format(self.bet))
            self.bet = 0
        else:
            self.money += self.bet
            text_effects.writing_effect("Congratulations! You won ${}!".format(self.bet))
            self.bet = 0
    
    def busted(self):
        self.bust = True

    def pair(self):
        self.pairs = True
    
    def has_ace(self):
        self.ace = True

    def double_d(self):
        self.double_down == True
    
    def erase_sum(self):
        self.sum_of_cards = 0
        self.ace = False

    def sum_cards_hand(self):
        values = []
        aces = []
        non_nums = {
        "J" : 10,
        "Q" : 10,
        "K" : 10,
        "A" : 11
    }
        for card in self.cards_in_hand:
            values.append(card[:1])
        
        while "A" in values:
            ace_idx = values.index("A")
            ace_letter = values.pop(ace_idx)
            aces.append(ace_letter)

        for value in values:
            try:
                self.sum_of_cards += int(value)
            except ValueError:
                self.sum_of_cards += 10
                
        if bool(aces) == True:
            for ace in aces:
                if self.ace == True and (len(aces) > 1):
                    self.sum_of_cards += 1
                elif self.sum_of_cards + 12 > 21 and (len(aces) > 1):
                    self.sum_of_cards += 1
                    self.has_ace()
                elif self.sum_of_cards + 11 > 21:
                    self.sum_of_cards += 1
                    self.has_ace()
                else:
                    self.sum_of_cards += 11
                    self.has_ace()
    
    def win_lose(self):
        losing_txt = "Oof, looks like you didn't make the cut!"
        if self.sum_of_cards > 21:
            text_effects.writing_effect("")
            self.game_over = True
        if self.sum_of_cards == 21 and len(self.cards_in_hand) == 2:
            self.blackjack = True
            self.win()
        if self.sum_of_cards == 21:
            self.win()
        


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
        player.erase_sum()
        for i in range(2):
            card = shuffled_deck.pop()
            card_pile.append(card)
            player.cards_in_hand.append(card)

def deal_one(shuffled_deck, card_pile, player):
    player.erase_sum()
    card = shuffled_deck.pop()
    card_pile.append(card)
    player.cards_in_hand.append(card)


def return_pile(card_pile, used_deck):
    for card in card_pile:
        used_deck.append(card)
    return used_deck

def player_turn(turn, shuffled_deck, card_pile, player):
    if turn.lower() == "hit":
        deal_one(shuffled_deck, card_pile, player)
        
    elif turn.lower() == "stand":
        pass
    elif turn.lower() == "doubledown" and player.sum_of_cards in range(9, 12):
        player.double_d()
        deal_one(shuffled_deck, card_pile, player)
    
