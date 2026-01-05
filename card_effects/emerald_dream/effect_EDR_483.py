"""Effect for Fractured Power (EDR_483).

Card Text: Destroy one of your Mana Crystals.
In 2 turns, gain two.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()