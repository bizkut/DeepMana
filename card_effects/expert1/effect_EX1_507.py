"""Effect for Murloc Warleader (EX1_507).

Card Text: Your other Murlocs have +2 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2