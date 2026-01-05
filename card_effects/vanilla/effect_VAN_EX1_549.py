"""Effect for Bestial Wrath (VAN_EX1_549).

Card Text: Give a Beast +2 Attack and <b>Immune</b> this turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2