"""Effect for Corrupting Mist (UNG_831).

Card Text: Curse all minions. Destroy them at the start of your next turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()