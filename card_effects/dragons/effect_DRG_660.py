"""Effect for Galakrond, the Unspeakable (DRG_660).

Card Text: [x]<b>Battlecry:</b> Destroy 1
random enemy minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    if opponent.board: random.choice(list(opponent.board)).destroy()