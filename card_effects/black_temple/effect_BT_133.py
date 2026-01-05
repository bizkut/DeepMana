"""Effect for Marsh Hydra (BT_133).

Card Text: [x]<b>Rush</b>
After this attacks, add a
random 8-Cost minion
to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass