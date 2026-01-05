"""Effect for Bonelord Frostwhisper (RLK_591).

Card Text: <b>Deathrattle:</b> For the rest of the game, your first card each turn costs (0). You die in 3 turns.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass