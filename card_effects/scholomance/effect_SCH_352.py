"""Effect for Potion of Illusion (SCH_352).

Card Text: Add 1/1 copies of your minions to your hand. They cost (1).
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass