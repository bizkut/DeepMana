"""Effect for Plague of Death (ULD_718).

Card Text: <b>Silence</b> and destroy all minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()