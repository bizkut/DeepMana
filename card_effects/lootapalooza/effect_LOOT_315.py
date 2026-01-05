"""Effect for Trogg Gloomeater (LOOT_315).

Card Text: <b>Taunt</b>
<b>Poisonous</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass