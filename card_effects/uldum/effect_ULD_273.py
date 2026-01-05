"""Effect for Overflow (ULD_273).

Card Text: Restore #5 Health
to all characters.
Draw 5 cards.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(5)