"""Effect for Vicious Bloodworm (RLK_711).

Card Text: [x]<b>Battlecry:</b> Give a minion in
your hand Attack equal to
this minion's Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1