"""Effect for Forsaken Lieutenant (AV_601).

Card Text: <b><b>Stealth</b>.</b> After you play
a <b>Deathrattle</b> minion, become a 2/2 copy of it with <b>Rush</b>.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass