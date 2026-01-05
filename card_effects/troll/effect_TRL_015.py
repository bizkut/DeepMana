"""Effect for Ticket Scalper (TRL_015).

Card Text: <b>Overkill</b>: Draw 2 cards.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)