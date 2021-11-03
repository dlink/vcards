#!/bin/env python
# -*- coding: utf-8 -*-

from random import randint

class VCards():

    def __init__(self):
        self.cards = self.loadCards()

    def loadCards(self):
        cards = []
        card0 = Card('English', 'Japanese',
                     '1', '一')
        
        card01 = Card('English', 'Japanese',
                     '2', '二')
        
        card1 = Card('English', 'Japanese',
                     'What time is it?',
                     '何時ですか')
        card2 = Card('English', 'Japanese',
                     'Where are you going?',
                     'どこに行きますか')
        cards.append(card0)
        cards.append(card01)
        cards.append(card1)
        cards.append(card2)
        return cards

    def test(self):
        n = 0
        correct = 0
        queue = self.cards
        while queue:
            n += 1

            # get random card from queu
            card_num = randint(1, len(queue))-1
            card = queue[card_num]
            del queue[card_num]

            # print card
            ind = self.printCard(n, card)

            # get answer
            ans = input(ind + card.back_name + ": ")

            # break out if nec.
            if ans == 'q':
                print('End Session')
                break
            print()

            # check answer
            if ans == card.back:
                correct += 1
                print(ind + 'Correct')
            else:
                print(ind + 'Incorrect. %s' % card.back)

            # show score
            print("%sScore: %s/%s" % (ind, correct, n))
            print()
            
    def printCard(self, n, card):
        nstr = str(n)
        ind = ' ' * (len(nstr)+2)
        print('%s.--%s--.' % (ind, '-'*len(card.front)))
        print('%s  |  %s  |' % (nstr, card.front))
        print('%s.--%s--.' % (ind, '-'*len(card.front)))
        return ind

class Card():

    def __init__(self, front_name, back_name, front, back):
        self.front_name = front_name
        self.back_name = back_name
        self.front = front
        self.back = back

if __name__ == '__main__':
    VCards().test()
    
