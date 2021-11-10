#!/bin/env python
# -*- coding: utf-8 -*-

import csv
from random import randint

from vlib.cli import CLI
from vlib.utils import validate_num_args

class VCardsError(Exception): pass

class VCards():

    def __init__(self):
        #self.cards = self.loadCards()
        self.verbose = 0

    def run(self):
        '''Set up Command Line (CLI) commands and options
           launch CLI process
        '''
        commands =  ['run <card_data.csv> [back]']
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
        if cmd == 'run':
            validate_num_args('run', 1, args)
            data_filename = args.pop(0)
            test_side = 'front'
            if args:
                test_side = args.pop(0)
                if test_side != 'back':
                    raise VCardsError('Unrecognized arg: %s' % test_side)
            return self.runCards(data_filename, test_side)

        raise VCardsError('Unrecognized command: %s' % cmd)

    def runCards(self, data_filename, test_side='front', repeat_errors=1):
        cards = self.loadCardData(data_filename)
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
        queue = cards
        repeat = 0
        while queue:

            # get random card from queu
            if not repeat:
                card_num = randint(1, len(queue))-1
                card = queue[card_num]
                del queue[card_num]
                n += 1

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
            if check_guess(guess, answer):
                print(ind + 'Correct')
                if not repeat:
                    correct += 1
                repeat = 0
            else:
                print(ind + 'Incorrect. %s' % answer)
                if repeat_errors:
                    repeat = 1

            # show score
            print("%sScore: %s/%s" % (ind, correct, n))
            print()

    def loadCardData(self, data_filename):
        data = []
        for i, row in enumerate(csv.reader(open(data_filename, 'r'))):
            # skip header:
            if i == 0:
                continue
            card = Card(*row)
            data.append(card)
        return data

    def printCard(self, n, question):
        nstr = str(n)
        ind = ' ' * (len(nstr)+2)
        print('%s.--%s--.' % (ind, '-'*len(question.encode('utf-8'))))
        print('%s  |  %s  |' % (nstr, question))
        print('%s.--%s--.' % (ind, '-'*len(question.encode('utf-8'))))
        return ind

def check_guess(guess, answer):
    guess2 = guess.lower().\
        replace('.', '') # remove periods
    answer2 = answer.lower()
    return guess2 == answer2

class Card():

    def __init__(self, front_name, front, back_name, back):
        self.front_name = front_name
        self.front = front
        self.back_name = back_name
        self.back = back

if __name__ == '__main__':
    VCards().run()
