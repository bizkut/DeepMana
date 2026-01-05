"""Effect for Activate the Obelisk (ULD_724).

Card Text: <b>Quest:</b> Restore 15 Health.
<b>Reward:</b> Obelisk's Eye.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 15, source)