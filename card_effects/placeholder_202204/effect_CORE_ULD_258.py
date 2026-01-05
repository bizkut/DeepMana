"""Effect for Armagedillo (CORE_ULD_258).

Card Text: [x]<b>Taunt</b>
At the end of your turn,
give all <b>Taunt</b> minions
in your hand +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2