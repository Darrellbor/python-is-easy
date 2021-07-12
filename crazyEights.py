#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Title: CrazyEights.py
    Description: This file demonstrates my understanding of the 
    final project and exam section of python is easy course
"""

from random import shuffle

playerName = ''

class CrazyEights:
    """Create a class to store all methods and objects"""

    def __init__(self):
        self.suits = ['h','d','s','c']
        self.cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self.value = [2,3,4,5,6,7,50,9,10,10,10,10,10]
        self.stock = list((x,y) for x in self.suits for y in self.cards)
        self.player_hand = []
        self.dealer_hand = []
        self.discard_pile = 0
        self.new_suit = ''
    
    def deal_cards(self):
        shuffle(self.stock)
        for i in range(7):
            self.player_hand.append(self.stock.pop())
            self.dealer_hand.append(self.stock.pop())
        self.discard_pile = self.stock.pop()
    
    def card_value(self, card):
        return self.value[self.cards.index(card[1])]
    
    def player_discard(self, inpt):
        """
        The function determines whether player's selected card qualifies for
        discard or not
        
        """
        
        if inpt.isdigit() == False:
            return 0
        if int(inpt) > len(self.player_hand):
            print("\nNumber of card entered is greater than number of cards")
            print("Please try again \n")
            return 0
        if self.player_hand[int(inpt)-1][1] == '8':
            self.discard_pile = self.player_hand.pop(int(inpt)-1)
            self.new_suit = ''
            while self.new_suit not in ['h','d','s','c']:
                self.new_suit = input("Please enter new suit: h, d, s, c\n")
            print("\nNew suit is: ", self.new_suit)
            return 1
        if self.new_suit != '':
            if self.player_hand[int(inpt)-1][0] == self.new_suit:
                self.discard_pile = self.player_hand.pop(int(inpt)-1)
                self.new_suit = ''
                return 1
            else:
                print("\nYou need to match new suit")
                print("Please try again\n")
                return 0
        if self.new_suit == '':
            if self.player_hand[int(inpt)-1][0] == self.discard_pile[0] or \
            self.player_hand[int(inpt)-1][1] == self.discard_pile[1]:
                self.discard_pile = self.player_hand.pop(int(inpt)-1)
                return 1
            else:
                print("\nYou need to match discard pile card suit or rank")
                print("Please try again\n")
                return 0
    
    def player_play(self):
        disc = 0
        inpt = ''
        global playerName
        print("\n{}'s turn".format(playerName))
        
        while disc == 0 and len(self.stock) > 0:
            print("{}'s cards: \n".format(playerName), self.player_hand)
            print("Discard pile: ", self.discard_pile)
            inpt = input("Please enter 0 if you need another card or number "\
                              "of card to discard\n")
            if inpt == '0':
                self.player_hand.append(self.stock.pop())
            elif inpt == '--help':
                print('Eight cards are dealt to each player (or seven in a two-player game).[4] The remaining cards of the deck are placed face down at the center of the table. The top card is then turned face up to start the game. Players discard by matching rank or suit with the top card of the discard pile, starting with the player left of the dealer. They can also play any 8 at any time. If a player is unable to match the rank or suit of the top card of the discard pile and does not have an 8, they draw cards from the stockpile until they get a playable card. When a player plays an 8, they must declare the suit that the next player is to play; that player must then follow the named suit or play another 8. \n The game ends as soon as one player has emptied their hand. That player collects a payment from each opponent equal to the point score of the cards remaining in that opponent\'s hand. 8s score 50, court cards 10 and all other cards face value')
            elif inpt == '--resume':
                continue
            else:
                disc = self.player_discard(inpt)
        if len(self.player_hand) == 0:
            print("{} is out of cards".format(playerName))
            return
        elif len(self.stock) == 0:
            print("No cards in stock pile")
            return
        else:
            print("------------------------------------------------")
            self.dealer_play()
            
    def dealer_matching(self):
        """
        The function determines whether dealer has a card that would qualify for
        discard or not
        
        """
        if len([card for card in self.dealer_hand if card[1] == '8']) > 0:
            self.discard_pile = [card for card in self.dealer_hand if card[1] == '8'][0]
            self.dealer_hand.remove(self.discard_pile)
            dealer_suits = [card[0] for card in self.dealer_hand]
            self.new_suit = max(set(dealer_suits), key=dealer_suits.count)
            print("\nNew suit is :", self.new_suit)
            return 1
        if self.new_suit != '':
            matching = []
            for card in self.dealer_hand:
                if card[0] == self.new_suit:
                    matching.append(card)
            if len(matching) > 0:
                matching_values = list(map(self.card_value, matching))
                self.discard_pile = matching[matching_values.index(max(matching_values))]
                self.dealer_hand.remove(self.discard_pile)
                self.new_suit = ''
                return 1
            else:
                return 0
        if self.new_suit == '':
            matching = []
            for card in self.dealer_hand:
                if card[0] == self.discard_pile[0] or card[1] == self.discard_pile[1]:
                    matching.append(card)
            if len(matching) > 0:
                matching_values = list(map(self.card_value, matching))
                self.discard_pile = matching[matching_values.index(max(matching_values))]
                self.dealer_hand.remove(self.discard_pile)
                return 1
            else:
                return 0
        
    def dealer_play(self):
         disc = 0
         print("\nDealer's turn")
         
         i = 0
         while disc == 0 and len(self.stock) > 0:
             #print("Dealer's cards: \n", self.dealer_hand)
             #print("Discard pile: ", self.discard_pile)
            
             disc = self.dealer_matching()
             if disc == 0:
                 self.dealer_hand.append(self.stock.pop())
                 i +=1
         print("Dealer drew {} cards".format(i))
         if len(self.dealer_hand) == 0:
             print("Dealer is out of cards")
             return
         elif len(self.stock) == 0:
             print("No cards in stock pile")
             return
         else:
             print("------------------------------------------------")
             self.player_play()
    
    def calc_points(self):
        player_points = 0
        dealer_points = 0
        global playerName
        for card in self.player_hand:
            player_points += self.card_value(card)
        for card in self.dealer_hand:
            dealer_points += self.card_value(card)
        
        print("\n{} points: ".format(playerName), player_points)
        print("Dealer points: ", dealer_points)
        if player_points < dealer_points:
            print("{} wins".format(playerName))
        else:
            print("Dealer wins") 
            
    def start(self):
        self.deal_cards()
        self.player_play()
        self.calc_points()


game = CrazyEights()
playerName = input("Please enter your name: ")
game.start()