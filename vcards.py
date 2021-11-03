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

    def test(self, test_side='front'):
        if test_side == 'front':
            question = 'front'
            answer = 'back'
            answer_name = 'back_name'
        else:
            question = 'back'
            answer = 'front'
            answer_name = 'front_name'

        n = 0
        correct = 0
        queue = self.cards
        while queue:
            n += 1

            # get random card from queu
            card_num = randint(1, len(queue))-1
            card = queue[card_num]
            del queue[card_num]

            if test_side == 'front':
                question = card.front
                answer = card.back
                answer_name = card.back_name
            else:
                question = card.back
                answer = card.front
                answer_name = card.front_name

            # print card
            ind = self.printCard(n, question)

            # get answer
            guess = input(ind + answer_name + ": ")

            # break out if nec.
            if guess == 'q':
                print('End Session')
                break
            print()

            # check answer
            if guess.lower() == answer.lower():
                correct += 1
                print(ind + 'Correct')
            else:
                print(ind + 'Incorrect. %s' % answer)

            # show score
            print("%sScore: %s/%s" % (ind, correct, n))
            print()
            
    def printCard(self, n, question):
        nstr = str(n)
        ind = ' ' * (len(nstr)+2)
        print('%s.--%s--.' % (ind, '-'*len(question.encode('utf-8'))))
        print('%s  |  %s  |' % (nstr, question))
        print('%s.--%s--.' % (ind, '-'*len(question.encode('utf-8'))))
        return ind

class Card():

    def __init__(self, front_name, back_name, front, back):
        self.front_name = front_name
        self.back_name = back_name
        self.front = front
        self.back = back

if __name__ == '__main__':
    VCards().test('back')
    
