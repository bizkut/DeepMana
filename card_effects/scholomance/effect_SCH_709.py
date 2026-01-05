"""Effect for Smug Senior (SCH_709).

Card Text: <b>Taunt</b>. <b>Deathrattle:</b> Add a 5/7 Ghost with <b>Taunt</b> to your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass