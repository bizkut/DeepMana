"""Effect for Meadowstrider (EDR_978).

Card Text: <b>Taunt</b>. <b>Deathrattle:</b> Put
a Meadowstrider on the bottom of your deck. It costs (1).
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass