"""Effect for Cindersword (FIR_922).

Card Text: <b>Battlecry:</b> If you're holding a minion with
a <b>Dark Gift</b>, gain +3 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3