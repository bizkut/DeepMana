"""Effect for Leeching Poison (ICC_221).

Card Text: Give your weapon <b>Lifesteal</b> this turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1