"""Effect for The Lich King (CORE_ICC_314).

Card Text: [x]<b>Taunt</b>
At the end of your turn,
add a random <b>Lich King</b>
card to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass