"""Effect for Auctioneer Jaxon (SW_045).

Card Text: [x]Whenever you <b>Trade</b>,
<b>Discover</b> a card from your
 deck to draw instead.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)