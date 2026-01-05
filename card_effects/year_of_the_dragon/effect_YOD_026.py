"""Effect for Fiendish Servant (YOD_026).

Card Text: [x]<b>Deathrattle:</b> Give this
minion's Attack to a random
friendly minion.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1