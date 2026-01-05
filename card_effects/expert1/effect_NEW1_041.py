"""Effect for Stampeding Kodo (NEW1_041).

Card Text: <b>Battlecry:</b> Destroy a random enemy minion with 2 or less Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    if opponent.board: random.choice(list(opponent.board)).destroy()