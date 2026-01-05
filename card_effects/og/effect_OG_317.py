"""Effect for Deathwing, Dragonlord (OG_317).

Card Text: <b>Deathrattle:</b> Put all Dragons from your hand into the battlefield.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass