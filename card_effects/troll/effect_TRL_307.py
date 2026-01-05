"""Effect for Flash of Light (TRL_307).

Card Text: Restore #4 Health.
Draw a card.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(4)