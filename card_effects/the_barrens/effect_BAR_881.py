"""Effect for Invigorating Sermon (BAR_881).

Card Text: Give +1/+1 to all minions in your hand, deck, and battlefield.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1