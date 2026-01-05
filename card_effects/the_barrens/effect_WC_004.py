"""Effect for Fangbound Druid (WC_004).

Card Text: <b>Taunt</b>
<b>Deathrattle:</b> Reduce the Cost of a Beast in your hand by (2).
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass