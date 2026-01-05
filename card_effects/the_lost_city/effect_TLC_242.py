"""Effect for Ancient Stegodon (TLC_242).

Card Text: <b>Battlecry:</b> Choose to
gain <b>Taunt</b>, <b>Poisonous</b>,
or +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1