"""Effect for Sunfury Protector (VAN_EX1_058).

Card Text: <b>Battlecry:</b> Give adjacent minions <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1