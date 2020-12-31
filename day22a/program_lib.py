import re


def calculate(file_name):
   fo = open(file_name, "r+")
   lines = [parse_line(line.strip()) for line in fo.readlines()]
   player1_ix = lines.index("Player 1:")
   player2_ix = lines.index("Player 2:")
   deck1 = [int(x) for x in lines[player1_ix+1:player2_ix-1]]
   deck2 = [int(x) for x in lines[player2_ix+1:]]
   
   while len(deck1) > 0 and len(deck2) > 0:
      deck1, deck2 = round(deck1, deck2)

   winner_deck = deck2 if len(deck2) > 0 else deck1

   result = [x * (len(winner_deck) - i) for i, x in enumerate(winner_deck)]

   return sum(result)

def round(deck1, deck2):
   card1 = deck1[0]
   card2 = deck2[0]

   if card1 > card2:
      res_deck1, res_deck2 = move_cards(deck1, deck2)
   else:
      res_deck2, res_deck1 = move_cards(deck2, deck1)
   return res_deck1, res_deck2

def move_cards(winner, loser):
   win_card = winner[0]
   los_card = loser[0]

   res_winner = winner[1:]
   res_loser = loser[1:]

   res_winner.append(win_card)
   res_winner.append(los_card)

   return res_winner, res_loser

def parse_line(line):
   return line
