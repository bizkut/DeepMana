"""Effect for King's Defender (AT_065).

Card Text: <b>Battlecry:</b> If you have a minion with <b>Taunt</b>, gain +1 Durability.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1