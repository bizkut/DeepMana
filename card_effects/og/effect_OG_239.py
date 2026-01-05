"""Effect for DOOM! (OG_239).

Card Text: Destroy all minions. Draw a card for each.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)