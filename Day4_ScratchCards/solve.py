from pprint import  pprint
with open('Day4_ScratchCards\\input.txt', 'r') as file:
    cards = file.readlines()
winning_nums = []
my_nums = []
card_dict = dict()
for i, card in enumerate(cards):
    card = card.strip()
    win, my = card.split('|')
    card_dict[i+1] = [win.split(':')[1].strip().split(), my.strip().split(), 1] # card_dict[card_no.] = [[win list],[my list],[quantity]]

for card in card_dict:
    matches = 0
    for num in card_dict[card][1]:
        if num in card_dict[card][0]: #and (card+matches < 213):
            matches += 1
            card_dict[card+matches][2] += 1*card_dict[card][2]
            
total_cards = 0
for card in card_dict:
    total_cards += card_dict[card][2]
pprint(total_cards)