"""Effect for Mortuary Machine (ULD_702).

Card Text: After your opponent plays a minion, give it <b>Reborn</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1