"""Effect for Siegebreaker (EX1_185).

Card Text: <b>Taunt</b>
Your other Demons have +1 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1