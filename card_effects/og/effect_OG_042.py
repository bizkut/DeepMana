"""Effect for Y'Shaarj, Rage Unbound (OG_042).

Card Text: At the end of your turn, put a minion from your deck into the battlefield.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass