"""Effect for Unidentified Contract (DAL_366).

Card Text: Destroy a minion. Gains a bonus effect in your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()