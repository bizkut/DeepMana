"""Effect for Shadow Word: Forbid (WON_064).

Card Text: <b>Tradeable</b>
Destroy a 4-Attack minion. <b>Corrupt:</b> Destroy ALL 4-Attack minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()