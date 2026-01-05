"""Effect for Bite (VAN_EX1_570).

Card Text: Give your hero +4 Attack this turn. Gain 4 Armor.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 4
        target._max_health += 4