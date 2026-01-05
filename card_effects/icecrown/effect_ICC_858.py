"""Effect for Bolvar, Fireblood (ICC_858).

Card Text: <b>Divine Shield</b>
After a friendly minion loses <b>Divine Shield</b>, gain +2 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2