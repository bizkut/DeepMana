"""Effect for Grand Crusader (AT_118).

Card Text: <b>Battlecry:</b> Add a random Paladin card to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass