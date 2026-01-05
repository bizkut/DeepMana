"""Effect for Dragonmaw Poacher (DRG_063).

Card Text: <b>Battlecry:</b> If your opponent controls a Dragon, gain +4/+4 and <b>Rush</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 4
        target._max_health += 4