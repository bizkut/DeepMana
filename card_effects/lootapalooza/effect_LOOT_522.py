"""Effect for Crushing Walls (LOOT_522).

Card Text: Destroy your opponent's left and right-most minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()