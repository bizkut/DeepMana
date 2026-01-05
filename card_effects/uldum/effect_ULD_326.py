"""Effect for Bazaar Burglary (ULD_326).

Card Text: [x]<b>Quest:</b> Add 4 cards from
other classes to your hand.
<b>Reward: </b>Ancient Blades.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass