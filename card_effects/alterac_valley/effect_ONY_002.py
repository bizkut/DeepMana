"""Effect for Gear Grubber (ONY_002).

Card Text: <b>Taunt</b>. If you end your turn with any unspent Mana, reduce this card's Cost by (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass