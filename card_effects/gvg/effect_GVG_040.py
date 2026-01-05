"""Effect for Siltfin Spiritwalker (GVG_040).

Card Text: Whenever another friendly Murloc dies, draw a card. <b><b>Overload</b>:</b> (1)
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)