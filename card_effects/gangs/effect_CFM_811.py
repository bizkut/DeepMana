"""Effect for Lunar Visions (CFM_811).

Card Text: Draw 2 cards. Minions drawn cost (2) less.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)