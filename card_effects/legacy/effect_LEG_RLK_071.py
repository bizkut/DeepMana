"""Effect for Patchwerk (LEG_RLK_071).

Card Text: [x]<b>Battlecry:</b> Destroy a random
minion in your opponent's
 hand, deck, and battlefield. 
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    if opponent.board: random.choice(list(opponent.board)).destroy()