"""Effect for Blingtron 3000 (GVG_119).

Card Text: <b>Battlecry:</b> Equip a random weapon for each player.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass