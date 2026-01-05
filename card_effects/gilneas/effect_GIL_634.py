"""Effect for Bellringer Sentry (GIL_634).

Card Text: <b>Battlecry and Deathrattle:</b> Put a <b>Secret</b> from your deck into the battlefield.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass


def deathrattle(game, source):
    pass