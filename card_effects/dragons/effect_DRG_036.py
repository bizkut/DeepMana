"""Effect for Waxadred (DRG_036).

Card Text: [x]<b>Deathrattle:</b> Shuffle a
Candle into your deck that
resummons Waxadred
when drawn.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    player.draw(1)