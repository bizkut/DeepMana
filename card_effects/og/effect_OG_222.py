"""Effect for Rallying Blade (OG_222).

Card Text: <b>Battlecry:</b> Give +1/+1 to your minions with <b>Divine Shield</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1