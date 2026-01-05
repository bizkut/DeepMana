"""Effect for Recruiter (AT_113).

Card Text: <b>Inspire:</b> Add a 2/2 Squire to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass