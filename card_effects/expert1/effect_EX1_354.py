"""Effect for Lay on Hands (EX1_354).

Card Text: Restore #8 Health. Draw 3 cards.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(8)