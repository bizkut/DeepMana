"""Effect for Mechanical Yeti (GVG_078).

Card Text: <b>Deathrattle:</b> Give each player a <b>Spare Part.</b>
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1