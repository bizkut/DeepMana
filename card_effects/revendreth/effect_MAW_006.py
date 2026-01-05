"""Effect for Objection! (MAW_006).

Card Text: <b>Secret:</b> When your opponent plays a
 minion, <b>Counter</b> it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass