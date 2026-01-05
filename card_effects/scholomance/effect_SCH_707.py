"""Effect for Fishy Flyer (SCH_707).

Card Text: <b>Rush</b>. <b>Deathrattle:</b> Add a 4/3 Ghost with <b>Rush</b> to your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass