"""Effect for Pride Seeker (AV_296).

Card Text: [x]<b>Battlecry:</b> Your next
<b>Choose One</b> card costs
(2) less.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass