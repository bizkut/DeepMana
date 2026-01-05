"""Effect for Sira'kess Cultist (TSC_955).

Card Text: <b>Battlecry:</b> Give
your opponent an
Abyssal Curse.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1