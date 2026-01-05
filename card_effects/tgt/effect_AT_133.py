"""Effect for Gadgetzan Jouster (AT_133).

Card Text: <b>Battlecry:</b> Reveal a minion in each deck. If yours costs more, gain +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1