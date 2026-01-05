"""Effect for Whirlpool (TSC_209).

Card Text: Destroy all minions and all copies of them <i>(wherever they are)</i>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()