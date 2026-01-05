"""Effect for First Day of School (SCH_247).

Card Text: Add 2 random 1-Cost minions to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass