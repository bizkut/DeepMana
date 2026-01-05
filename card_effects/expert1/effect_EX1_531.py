"""Effect for Scavenging Hyena (EX1_531).

Card Text: Whenever a friendly Beast dies, gain +2/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2