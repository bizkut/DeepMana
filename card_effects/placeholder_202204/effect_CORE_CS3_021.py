"""Effect for Enslaved Fel Lord (CORE_CS3_021).

Card Text: <b>Taunt</b>. Also damages the minions next to whomever this attacks.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass