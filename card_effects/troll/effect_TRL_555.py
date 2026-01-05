"""Effect for Demonbolt (TRL_555).

Card Text: Destroy a minion. Costs (1) less for each minion you control.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()