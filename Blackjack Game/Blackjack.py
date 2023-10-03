import random

# CARDS have SUITS, RANKS and VALUES
suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two', 'Three', 'Four', "Five", 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 
          'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, "Five":5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 
          'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

# CARD CLASS
class Card():
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit

# DECK CLASS
class Deck:
    
    def __init__(self):
        
        self.deck = []
        
        for suit in suits:
            for rank in ranks:
                # Add the created card object into Deck
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n'+ card.__str__()
        return "The deck has: "+deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()

# HAND CLASS
class Hand:
    
    def __init__(self):

        self.cards = []
        self.value = 0
        self.aces = 0
        
    def add_card(self,card):
        
        if card.rank == 'Ace':
            self.aces += 1
        
        self.cards.append(card)
        self.value += card.value


    def adjust_for_ace(self):
        
        while self.aces and self.value > 21: 
            self.value -= 10
            self.aces -= 1

# CHIPS CLASS
class Chips:
    
    def __init__(self,total = 100):

        self.total = 100
        self.bet = 0
        
    def win_bet(self):
        
        self.total += self.bet

    def lose_bet(self):
        
        self.total -= self.bet

# Functions for gameplay
def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except ValueError:
            print("Enter an integer value for bet!")
        else:
            if chips.bet > chips.total:
                print("Not enough chips! Your bet can't exceed",chips.total)
            else:
                break

def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    
    global playing 
    
    while True:
        x = input('Hit or Stand? Enter H or S ')
        
        if x[0].upper() == 'H':
            hit(deck,hand)
        elif x[0].upper() == 'S':
            print("Player Stands Dealer's Turn")
            playing = False
        else:
            print("Not valid input! Please enter H or S only!")
            continue
        break

def show_some(player,dealer):
    
    # Show only one of dealer's cards
    print("\n Dealer's Hand: ")
    print("First card hidden!")
    print(dealer.cards[1])
    
    # Show all cards of the player's cards
    print("\n Player's Hand: ")
    for card in player.cards:
        print(card)
      
def show_all(player,dealer):
    
    # Show all the dealer's cards
    print("\n Dealer's Hand: ",*dealer.cards,sep='\n')   
    
    # Calculate and display value
    print(f"Value of Dealer's hand is: {dealer.value}")
    
    # Show all cards of the player's cards
    print("\n Player's Hand: ",*player.cards,sep='\n')
        
    # Calculate and display value
    print(f"Value of Player's hand is: {player.value}")

def player_busts(player,dealer,chips):
    print("BUST PLAYER!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("PLAYER WINS!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("PLAYER WINS! DEALER BUSTED!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("DEALER WINS!")
    chips.lose_bet()

def push(player,dealer):
    print('Dealer and Player tie! PUSH')


while True:
    
    print("\nWELCOME TO BLACKJACK! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.")
    
    # Create and shuffle deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    # Set up Player's chips
    player_chips = Chips()
    
    # Prompt the Player for bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing: # recall this variable from hit_or_stand function
        
        if player_hand.value == 21:
            print("BLACKJACK")
            player_wins(player_hand,dealer_hand,player_chips)
            break
            
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
        
        # If Player's hand exceeds 21, Player busts
        if player_hand.value > 21:
            # Show all cards
            show_all(player_hand,dealer_hand)
            player_busts(player_hand,dealer_hand,player_chips)
            break
    
    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
            
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
        
        # Show all cards
        show_all(player_hand,dealer_hand)

        # Run different winning scenearios
        if player_hand.value == 21:
            print("BLACKJACK")
            player_wins(player_hand,dealer_hand,player_chips)
        
        elif dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
          
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        
        else:
            push(player_hand,dealer_hand)
        
    # Inform Player of their chips total
    print(f"\n Player total chips are at: {player_chips.total}")
        
    # Ask play again
    new_game = input("Would you like to play another hand? 'y' or 'n' ")
       
    if new_game[0].lower()=='y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break
