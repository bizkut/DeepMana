"""Effect for Armor Vendor (YOP_032).

Card Text: <b>Battlecry:</b> Give 4 Armor to each hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 4
        target._max_health += 4