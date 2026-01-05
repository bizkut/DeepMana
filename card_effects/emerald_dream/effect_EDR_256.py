"""Effect for Dreamwarden (EDR_256).

Card Text: [x]<b>Taunt</b>. <b>Battlecry:</b> If there
is a card in your deck that
didn't start there, draw it
and gain +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)