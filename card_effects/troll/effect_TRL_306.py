"""Effect for Immortal Prelate (TRL_306).

Card Text: <b>Deathrattle:</b> Shuffle this into your deck. It keeps any enchantments.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass