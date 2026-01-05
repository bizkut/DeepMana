"""Effect for Bootstrap Sunkeneer (TSC_933).

Card Text: [x]<b>Combo:</b> Put an enemy
minion on the bottom of
 your opponent's deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass