"""Effect for Bottomfeeder (TSC_653).

Card Text: <b>Deathrattle:</b> Add a Bottomfeeder to the bottom of your deck with permanent +2/+2.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2