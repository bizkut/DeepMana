"""Effect for Defender of Argus (CORE_EX1_093).

Card Text: <b>Battlecry:</b> Give adjacent minions +1/+1 and <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1