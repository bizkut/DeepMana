"""Effect for Rin, the First Disciple (LOOT_415).

Card Text: <b>Taunt</b>
<b>Deathrattle:</b> Add 'The First Seal' to your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass