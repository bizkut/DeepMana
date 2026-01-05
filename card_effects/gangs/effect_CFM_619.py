"""Effect for Kabal Chemist (CFM_619).

Card Text: <b>Battlecry:</b> Add a random Potion to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass