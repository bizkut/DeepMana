"""Effect for Rotnest Drake (YOD_036).

Card Text: [x]<b>Battlecry:</b> If you're holding
a Dragon, destroy a random
enemy minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    if opponent.board: random.choice(list(opponent.board)).destroy()