"""Effect for Twisting Nether (CORE_EX1_312).

Card Text: Destroy all minions
and locations.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()