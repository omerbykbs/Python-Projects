import random

# CARDS have SUITS, RANKS and VALUES

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two', 'Three', 'Four', "Five", 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 
          'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, "Five":5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 
          'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

# CARD CLASS

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit
    
# DECK CLASS

class Deck:
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                # Create the Card Object
                created_card = Card(suit,rank)
                
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()

# PLAYER CLASS

class Player:
    
    def __init__(self,name):

        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            # List of multiple card objects
            self.all_cards.extend(new_cards)
        else:
            # For a single card objects
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

# GAME SETUP

player_one = Player("One")
player_two = Player("Two")

# CREATING NEW DECK AND SHUFFLING CARDS IN DECK

new_deck = Deck()
new_deck.shuffle()

# DEALING THE CARDS TO TWO PLAYERS

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
    
game_on = True
round_num = 0

while game_on:
    
    round_num += 1
    print(f"Round {round_num}")
    
    # CHECK IF THE PLAYERS HAVE ANY CARDS TO PLAY
    if len(player_one.all_cards) == 0:
        print("Player One, out of cards! Player Two Wins!")
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print("Player Two, out of cards! Player One Wins!")
        game_on = False
        break
    
    # START A NEW ROUND AND RESET THE PLAYER CARDS ON THE TABLE
    
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    
    at_war = True
    
    while at_war:
        
        if player_one_cards[-1].value > player_two_cards[-1].value:
            
            # PLAYER ONE GETS THE CARDS
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            # WAR ENDS IN THIS ROUND
            at_war = False
        
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            
            # PLAYER TWO GETS THE CARDS
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            # WAR ENDS IN THIS ROUND
            at_war = False
            
        else:
            # CARDS VALUES ARE EQUAL 
            print('WAR!')
            
            # CHECK IF PLAYERS HAVE ENOUGH CARDS BEFORE GRABBING ANOTHER CARD
            if len(player_one.all_cards) < 7:
                print("Player One, unable to play war\nGame Over at War\nPLAYER TWO WINS!")
                game_on = False
                break
            
            elif len(player_two.all_cards) < 7:
                print("Player Two, unable to play war\nGame Over at War\nPLAYER ONE WINS!")
                game_on = False
                break
            
            # OTHERWISE WAR CONTINUES AND NEXT CARDS ARE ADDED
            else:
                for i in range(7):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
    
