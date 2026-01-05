"""Effect for Clean the Scene (REV_252).

Card Text: Destroy all minions with 3 or less Attack. <b>Infuse (3):</b> 6 or less.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()