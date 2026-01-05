"""Effect for Efficient Octo-bot (BAR_320).

Card Text: <b>Frenzy:</b> Reduce the Cost of cards in your hand by (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass