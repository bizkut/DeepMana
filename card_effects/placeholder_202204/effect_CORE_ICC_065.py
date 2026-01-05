"""Effect for Bone Baron (CORE_ICC_065).

Card Text: <b>Deathrattle:</b> Add two 1/1 Skeletons to your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass