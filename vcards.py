#!/bin/env python
# -*- coding: utf-8 -*-

from random import randint

from vlib.cli import CLI

class VCardsError(Exception): pass

class VCards():

    def __init__(self):
        self.cards = self.loadCards()
        self.verbose = 0

    def run(self):
        '''Set up Command Line (CLI) commands and options
           launch CLI process
        '''
        commands =  ['test']
        options = {}
        self.cli = CLI(self.process, commands, options)
        self.cli.process()

    def process(self, *args):
        '''Process all Incoming Requests
           Implement a catch all Exceptions
           Return status of process as a string
        '''
        if self.cli.hasoption.get('v'):
            self.verbose = 1

        args = list(args)
        cmd = args.pop(0)
        if cmd == 'test':
            return self.test()

        raise VCardsError('Unrecognized command: %s' % cmd)

    def loadCards(self):
        cards = []
        card1 = Card('English', 'Japanese',
                     '1', '一')
        card2 = Card('English', 'Japanese',
                     '2', '二')
        card3 = Card('English', 'Japanese',
                     'What time is it?',
                     '何時ですか')
        card4 = Card('English', 'Japanese',
                     'Where are you going?',
                     'どこへ行きますか')
        card5 = Card('English', 'Japanese',
                     'What is your name?', '名前は')
        cards.append(card1)
        cards.append(card2)
        cards.append(card3)
        cards.append(card4)
        cards.append(card5)
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
    VCards().run()
    
