"""Effect for Murder Accusation (CORE_MAW_019).

Card Text: Choose a minion. Destroy it after another enemy minion dies.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()