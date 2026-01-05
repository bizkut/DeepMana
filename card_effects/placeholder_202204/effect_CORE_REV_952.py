"""Effect for Sinful Sous Chef (CORE_REV_952).

Card Text: <b>Deathrattle:</b> Add 2
Silver Hand Recruits
to your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass