"""Effect for Click-Clocker (TSC_632).

Card Text: [x]<b>Divine Shield</b>. <b>Battlecry:</b>
Give a random Mech in
your hand +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1