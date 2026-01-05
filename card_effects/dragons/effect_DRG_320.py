"""Effect for Ysera, Unleashed (DRG_320).

Card Text: [x]<b>Battlecry:</b> Shuffle 7 Dream
Portals into your deck.
When drawn, summon
a random Dragon.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(7)