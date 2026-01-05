"""Effect for Acidmaw (WON_024).

Card Text: Whenever an enemy minion takes damage, destroy it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()