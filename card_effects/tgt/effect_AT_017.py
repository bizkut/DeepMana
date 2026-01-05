"""Effect for Twilight Guardian (AT_017).

Card Text: <b>Battlecry:</b> If you're holding a Dragon, gain +1 Attack and <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1