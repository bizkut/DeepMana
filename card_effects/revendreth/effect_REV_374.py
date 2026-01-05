"""Effect for Shadowborn (REV_374).

Card Text: <b>Deathrattle:</b> Reduce the Cost of the highest Cost Shadow spell in your hand by (3).
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass