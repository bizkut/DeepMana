"""Effect for Unseen Saboteur (DAL_538).

Card Text: <b>Battlecry:</b> Your opponent casts a random spell from their hand <i>(targets chosen randomly)</i>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass