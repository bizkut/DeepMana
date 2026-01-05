"""Effect for Luna's Pocket Galaxy (BOT_257).

Card Text: Change the Cost of minions in your
deck to (1).
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass