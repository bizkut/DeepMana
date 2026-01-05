"""Effect for Pogo-Hopper (BOT_283).

Card Text: [x]<b>Battlecry:</b> Gain +2/+2 for
each other Pogo-Hopper
you played this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2