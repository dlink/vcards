'''Convert lessions into csv files'''

import csv

file = '/home/dlink/japanese/pimsleur/30/food.txt'
#file = '/home/dlink/japanese/pimsleur/30/general_phrases.txt'
outfile = '/home/dlink/vcards/data/japanese_30food.csv'

out = csv.writer(open(outfile, 'w'))
out.writerow(['front_name', 'front', 'back_name', 'back'])
entries = []
romani = japanese = english = None
for i, line in enumerate(open(file, 'r').readlines()):
    line = line.strip()
    line = line.strip('.。')
    if not line:
        continue
    
    if romani and japanese:
        english = line
        entries.append([english, japanese])
        print([english, japanese])
        out.writerow(['English', english, 'Japanese', japanese])
        romani = japanese = english = None
    elif romani:
        japanese = line
    else:
        romani = line

    
