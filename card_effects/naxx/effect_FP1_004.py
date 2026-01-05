"""Effect for Mad Scientist (FP1_004).

Card Text: <b>Deathrattle:</b> Put a <b>Secret</b> from your deck into the battlefield.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass