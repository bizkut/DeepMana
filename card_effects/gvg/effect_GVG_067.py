"""Effect for Stonesplinter Trogg (GVG_067).

Card Text: Whenever your opponent casts a spell, gain +1 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1