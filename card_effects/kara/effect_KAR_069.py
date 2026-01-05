"""Effect for Swashburglar (KAR_069).

Card Text: <b>Battlecry:</b> Add a random card from another class to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass