#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import random
import itertools
import time
from functools import reduce
from IPython.display import clear_output


SUITS = ['H_', 'D_', 'S_', 'C_']
NUMS = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

CARDS = []
for x,y in itertools.product(SUITS, NUMS):
    CARDS.append(x+y)


class Game(object):
    
    def __init__(self, dealing=True, game=True):
        self.dealing = True
        self.game = True
    
    def change_game_state(self, sign):
        '''
        input:
            sign: yes/no for checking as str
        return:
            change the self.game
        '''
        if sign == 'n':
            self.game = False
        elif sign == 'y':
            self.game = True
    
    def judge(self, p_score, d_score):
        '''
        input:
            player score and dealer score as int
        return:
            ratio for updating the bankroll
        '''
        ratio = 0
        if p_score > 21:
            print("\nPLAYER BURST!!")
        elif p_score == 21 and d_score != 21:
            print("\nPLAYER BLACK JACK!!!!!")
            ratio = 2.5
        elif d_score > 12:
            print("\nDEALER BURST and PLAER WIN!!")
            ratio = 2
        elif p_score > d_score:
            print("\nPLAYER WIN!!!")
            ratio = 2
        elif p_score == d_score:
            print("\nDRAW")
            ratio = 1
        else:
            print("\nPLAYER LOSE...")
        
        return ratio


class Cards(object):
    
    def __init__(self, cards=CARDS):
        self.cards = cards
    
    def drawn(self, num):
        '''
        input:
            num: number of cards to be drawn
        return:
            drawn cards
        '''
        stuff = set( random.choice(self.cards, num, replace=True) )
        self.cards = list(set(self.cards) - stuff)
        
        return stuff
    
    def estimate(self, hands):
        '''
        input:
            hands: cards as list
        return:
            score: score of hands as int
        '''
        _cards = [ 10 if elem[2:] in ['J','Q','K']
            else int(elem[2:]) for elem in hands if elem[2:] != 'A'  ]
        _Anum = [ elem[2:] for elem in hands if elem[2:] == 'A' ]
        score = sum(_cards)
        
        for idx, elem in enumerate(_Anum, start=1):
            if not idx == len(_Anum):
                score += 1
            else:
                if score < 11:
                    score += 11
                else:
                    score += 1
        
        return score


class Player(object):
    
    def __init__(self, bankroll, hands=[]):
        self.bankroll = bankroll
        self.hands = hands
        
    def change_bankroll(self, amount):
        '''
        input:
            amount: amount for updating bankroll
        return:
            updated bankroll
        '''
        self.bankroll += amount
    
    def get_cards(self, stuff):
        '''
        input:
            cards as list
        return:
            updated hands
        '''
        self.hands.extend(stuff)
    
    def clear_cards(self):
        '''
        clear hands
        '''
        self.hands = []



if __name__ == '__main__':
    print("-----GAME START-----")
    game = Game()
    cards = Cards()
    player = Player(1000, [])
    dealer = Player(0, [])

    while game.game:
        player.clear_cards()
        dealer.clear_cards()

        print("\nBET your credit (your bankroll is {}):".format(player.bankroll))
        time.sleep(0.5); credit=int(input())
        player.change_bankroll(-credit)

        while game.dealing:
            player.get_cards( cards.drawn(2) )
            print("\nPLAYER CARDS:", player.hands)

            dealer.get_cards( cards.drawn(2) )
            print("DEALER CARDS:", [dealer.hands[0],"---"])

            if cards.estimate(player.hands) == 21:
                break

            print("\n(PLAYER turn) Choose your action, hit or stand or double:")
            time.sleep(0.5); action=input()

            if action == 'double':
                credit *= 2
                player.change_bankroll(-credit)
                player.get_cards( cards.drawn(1) )

            while action == 'hit':
                player.get_cards( cards.drawn(1) )
                print("\nPLAYER CARDS:", player.hands)

                if cards.estimate(player.hands) > 21:
                    break

                print("\n(PLAYER turn) Choose your action, hit or stand:")
                time.sleep(0.5); action=input()

            break


        while cards.estimate(dealer.hands) < 17:
            dealer.get_cards( cards.drawn(1) )

        print( "\nPLAYER CARDS:", player.hands )
        print( "DEALER CARDS:", dealer.hands )

        ratio = game.judge( cards.estimate(player.hands),cards.estimate(dealer.hands) )
        player.change_bankroll( ratio*credit )


        print("\nChoose y for continuing or n for finishing")
        sign = input()
        game.change_game_state(sign)
        clear_output()

    print("\nFinal bankroll: {}".format(player.bankroll))