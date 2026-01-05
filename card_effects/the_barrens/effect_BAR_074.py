"""Effect for Far Watch Post (BAR_074).

Card Text: [x]Can't attack. After your
opponent draws a card, it
   costs (1) more <i>(up to 10)</i>.  
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)