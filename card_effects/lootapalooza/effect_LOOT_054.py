"""Effect for Branching Paths (LOOT_054).

Card Text: [x]<b>Choose Twice -</b> Draw a
card; Give your minions 
+1 Attack; Gain 6 Armor.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)