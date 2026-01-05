"""Effect for Tundra Rhino (VAN_DS1_178).

Card Text: Your Beasts have <b>Charge</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass