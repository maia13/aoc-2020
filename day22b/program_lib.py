import re


def calculate(file_name):
   fo = open(file_name, "r+")
   lines = [parse_line(line.strip()) for line in fo.readlines()]
   player1_ix = lines.index("Player 1:")
   player2_ix = lines.index("Player 2:")
   deck1 = [int(x) for x in lines[player1_ix+1:player2_ix-1]]
   deck2 = [int(x) for x in lines[player2_ix+1:]]
   
   gtree = [0]
   pp(deck1, deck2, gtree, 'initial')

   winner, deck1, deck2 = game(deck1, deck2, gtree)
   winner_deck = deck1 if winner else deck2

   winner_deck.reverse()
   result = [x * (i + 1) for i, x in enumerate(winner_deck)]

   return sum(result)

def game(deck1, deck2, gtree):
   turn = 0
   set_decks1 = set()
   set_decks2 = set()
   subg = 0

   while len(deck1) > 0 and len(deck2) > 0:
      tdeck1 = tuple(deck1)
      tdeck2 = tuple(deck2)
      if tdeck1 in set_decks1 or tdeck2 in set_decks2:
         return True, deck1, deck2
      else:
         set_decks1.add(tdeck1)
         set_decks2.add(tdeck2)
      
      card1 = deck1[0]
      card2 = deck2[0]
      if card1 < len(deck1) and card2 < len(deck2):
         sub_deck1 = list(deck1[1:1+card1])
         sub_deck2 = list(deck2[1:1+card2])
         subgtree = list(gtree)
         subgtree.append(subg)
         subg += 1
         winner1, sub_deck1, sub_deck2 = game(sub_deck1, sub_deck2, subgtree)
         if winner1:
            deck1, deck2 = move_cards(card1, card2, deck1, deck2)
         else:
            deck2, deck1 = move_cards(card2, card1, deck2, deck1)
      else:
         deck1, deck2 = round(card1, card2, deck1, deck2)

      pp(deck1, deck2, gtree, turn)
      turn += 1 

   return len(deck1) > 0, deck1, deck2

def pp(deck1, deck2, game, turn):
   print(f'----- Game {game} | Turn {turn} -----')
   print(deck1)
   print(deck2)
   print()

def round(card1, card2, deck1, deck2):
   if card1 > card2:
      res_deck1, res_deck2 = move_cards(card1, card2, deck1, deck2)
   else:
      res_deck2, res_deck1 = move_cards(card2, card1, deck2, deck1)
   return res_deck1, res_deck2

def move_cards(win_card, los_card, winner, loser):
   res_winner = winner[1:]
   res_loser = loser[1:]

   res_winner.append(win_card)
   res_winner.append(los_card)

   return res_winner, res_loser

def parse_line(line):
   return line
