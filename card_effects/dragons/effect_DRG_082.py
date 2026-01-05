"""Effect for Kobold Stickyfinger (DRG_082).

Card Text: <b>Battlecry:</b> Steal your opponent's weapon.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass