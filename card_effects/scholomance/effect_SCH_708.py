"""Effect for Sneaky Delinquent (SCH_708).

Card Text: <b>Stealth</b>. <b>Deathrattle:</b> Add a 3/1 Ghost with <b>Stealth</b> to your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass