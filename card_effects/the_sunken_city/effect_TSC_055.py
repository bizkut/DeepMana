"""Effect for Seafloor Gateway (TSC_055).

Card Text: Draw a Mech. Reduce the Cost of Mechs in your hand by (1).
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)