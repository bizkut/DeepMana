"""Effect for Clockwork Gnome (GVG_082).

Card Text: <b>Deathrattle:</b> Add a <b>Spare Part</b> card to your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass