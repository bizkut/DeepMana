"""Effect for Voidcaller (FP1_022).

Card Text: <b>Deathrattle:</b> Put a random Demon from your hand into the battlefield.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass