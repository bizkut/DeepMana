"""Effect for Lady Deathwhisper (RLK_713).

Card Text: <b>Deathrattle:</b> Copy all
Frost spells in your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass