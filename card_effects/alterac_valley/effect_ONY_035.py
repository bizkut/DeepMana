"""Effect for Spawn of Deathwing (ONY_035).

Card Text: <b>Battlecry:</b> Destroy a random enemy minion. Discard a random card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    if opponent.board: random.choice(list(opponent.board)).destroy()