"""Effect for Aeroponics (DRG_314).

Card Text: Draw 2 cards.
Costs (2) less for each Treant you control.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)