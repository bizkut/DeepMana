"""Effect for Arcane Wyrm (RLK_548).

Card Text: <b>Battlecry:</b> Add an Arcane Bolt to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass