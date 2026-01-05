"""Effect for Wallow, the Wretched (EDR_487).

Card Text: While this is in your hand
or deck, it gains a copy of every <b>Dark Gift</b> given to your minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1