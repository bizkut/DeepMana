"""Effect for Ice Trap (AV_226).

Card Text: <b>Secret:</b> When your opponent casts a spell, return it to their hand instead. It costs (1) more.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass