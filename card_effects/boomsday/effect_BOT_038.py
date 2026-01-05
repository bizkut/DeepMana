"""Effect for Fireworks Tech (BOT_038).

Card Text: [x]<b>Battlecry:</b> Give a friendly
Mech +1/+1. If it has
<b>Deathrattle</b>, trigger it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1


def deathrattle(game, source):
    pass