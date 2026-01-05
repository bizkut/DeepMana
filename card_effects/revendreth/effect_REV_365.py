"""Effect for Convoke the Spirits (REV_365).

Card Text: [x]Cast 8 random
Druid spells <i>(targets
chosen randomly)</i>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass