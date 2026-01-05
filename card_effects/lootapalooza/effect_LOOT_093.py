"""Effect for Call to Arms (LOOT_093).

Card Text: [x]<b>Recruit</b> 3 minions that
 cost (2) or less.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass