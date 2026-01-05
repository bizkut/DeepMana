"""Effect for Dreampetal Florist (BOT_423).

Card Text: At the end of your turn, reduce the Cost of a random minion in your hand by (7).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass