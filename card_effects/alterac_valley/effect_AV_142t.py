"""Effect for Ivus, the Forest Lord (AV_142t).

Card Text: [x]<b>Battlecry:</b> Spend the rest of
your Mana and gain +2/+2,
<b>Rush</b>, <b>Divine Shield</b>, or <b>Taunt</b>
at random for each.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2