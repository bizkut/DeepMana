"""Effect for Bloodsail Raider (NEW1_018).

Card Text: <b>Battlecry:</b> Gain Attack equal to the Attack
of your weapon.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass