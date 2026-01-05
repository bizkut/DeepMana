"""Effect for The Soularium (BOT_568).

Card Text: Draw 3 cards.
They are <b>Temporary</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)