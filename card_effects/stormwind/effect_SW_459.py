"""Effect for Stormwind Piper (SW_459).

Card Text: After this minion attacks,
give your Beasts +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1