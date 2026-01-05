"""Effect for Crossroads Gossiper (BAR_890).

Card Text: After a friendly <b>Secret</b> is revealed, gain +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2