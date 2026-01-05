"""Effect for Hatchery Helper (TLC_233).

Card Text: [x]<b>Battlecry:</b> Give your
other minions with 2 or less
Attack +1/+2 and <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2