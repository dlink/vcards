Simple flash card program, that reads from csv files

Syntax:

     vcards.py [OPTIONS] run <card_data.csv> [back]
     
          back: test the back of the cards
          -v: Verbose
          -q: Quite

Example run:

     vcards.py run data/japanese.csv

        .----------------------------------------.
     1  |  How many days are you going to stay?  |
        .----------------------------------------.
        Japanese: 何日いますか
     
        Correct
        Score: 1/1
     
        .-----------------------------.
     2  |  I’m going to have lunch  |
        .-----------------------------.
        Japanese: q
     End Session
