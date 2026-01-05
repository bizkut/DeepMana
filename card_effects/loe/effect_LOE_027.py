"""Effect for Sacred Trial (LOE_027).

Card Text: <b>Secret:</b> After your opponent has at least 3 minions and plays another, destroy it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()