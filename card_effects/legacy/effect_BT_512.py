"""Effect for Inner Demon (BT_512).

Card Text: Give your hero +8 Attack this turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 8
        target._max_health += 8