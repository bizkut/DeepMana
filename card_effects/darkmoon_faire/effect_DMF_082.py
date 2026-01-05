"""Effect for Darkmoon Statue (DMF_082).

Card Text: Your other minions have +1 Attack. <b>Corrupt:</b> This gains +4 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1