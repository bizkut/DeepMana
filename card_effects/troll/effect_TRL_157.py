"""Effect for Walk the Plank (TRL_157).

Card Text: Destroy an undamaged minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()