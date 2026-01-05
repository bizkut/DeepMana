"""Effect for Shattering Blast (WC_041).

Card Text: Destroy all <b>Frozen</b> minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()