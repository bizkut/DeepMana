"""Effect for Grove Tender (GVG_032).

Card Text: <b>Choose One -</b> Give each player a Mana Crystal; or Each player draws a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)