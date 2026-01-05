"""Effect for Curse of Weakness (GIL_665).

Card Text: <b>Echo</b>
Give all enemy minions -2 Attack until your next turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2