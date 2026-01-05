"""Effect for Showstopper (DMF_191).

Card Text: <b>Deathrattle:</b> <b>Silence</b> all minions.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target: game.silence(target)