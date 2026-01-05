"""Effect for Embrace Darkness (CORE_ICC_849).

Card Text: [x]Choose an enemy minion.
At the start of your turn,
gain control of it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass