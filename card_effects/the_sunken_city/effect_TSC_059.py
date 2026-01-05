"""Effect for Bubblebot (TSC_059).

Card Text: [x]<b>Battlecry:</b> Give your other
Mechs <b>Divine Shield</b>
and <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1