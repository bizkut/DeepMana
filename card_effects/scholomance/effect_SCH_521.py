"""Effect for Coerce (SCH_521).

Card Text: Destroy a damaged minion. <b>Combo:</b> Destroy any minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()