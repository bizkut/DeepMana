"""Effect for Thistle Tea (OG_073).

Card Text: Draw a card. Add 2 extra copies of it to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)