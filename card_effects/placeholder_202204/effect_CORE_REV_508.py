"""Effect for Relic of Dimensions (CORE_REV_508).

Card Text: [x]Draw two cards 
and reduce their Cost 
by (1). Improve your 
future Relics.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)