"""Effect for Lakkari Sacrifice (UNG_829).

Card Text: [x]<b>Quest:</b> Discard 6 cards.
<b>Reward:</b> Nether Portal.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass