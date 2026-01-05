"""Effect for Plague of Wrath (CORE_ULD_707).

Card Text: Destroy all damaged minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()