"""Effect for Reincarnate (FP1_025).

Card Text: Destroy a minion,
then return it to life with full Health.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()