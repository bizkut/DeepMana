"""Effect for Kangor's Endless Army (BOT_912).

Card Text: Resurrect 3 friendly Mechs. They keep any <b>Magnetic</b> upgrades.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass