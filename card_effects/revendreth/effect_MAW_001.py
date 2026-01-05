"""Effect for Arson Accusation (MAW_001).

Card Text: Choose a minion. Destroy it after your hero takes damage.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()