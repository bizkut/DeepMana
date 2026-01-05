"""Effect for Kobold Monk (LOOT_382).

Card Text: Your hero is <b>Elusive</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass