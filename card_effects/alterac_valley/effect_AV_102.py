"""Effect for Popsicooler (AV_102).

Card Text: [x]<b>Deathrattle:</b> <b>Freeze</b> two
random enemy minions.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target: target.frozen = True