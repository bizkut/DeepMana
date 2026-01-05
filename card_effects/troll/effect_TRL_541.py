"""Effect for Hakkar, the Soulflayer (TRL_541).

Card Text: <b>Deathrattle:</b> Shuffle a Corrupted Blood into each player's deck.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass