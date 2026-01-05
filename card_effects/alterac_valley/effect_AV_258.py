"""Effect for Bru'kan of the Elements (AV_258).

Card Text: [x]<b>Battlecry:</b> Call upon the
power of two Elements!
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass