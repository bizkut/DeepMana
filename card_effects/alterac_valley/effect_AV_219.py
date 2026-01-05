"""Effect for Ram Commander (AV_219).

Card Text: [x]<b>Battlecry:</b> Add two
1/1 Rams with <b>Rush</b>
to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass