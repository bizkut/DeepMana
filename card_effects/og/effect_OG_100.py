"""Effect for Shadow Word: Horror (OG_100).

Card Text: Destroy all minions with 2 or less Attack.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()