"""Effect for Pounce (CORE_TRL_243).

Card Text: Give your hero +2 Attack this turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2