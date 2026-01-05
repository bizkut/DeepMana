"""Effect for Shadow Word: Ruin (EX1_197).

Card Text: Destroy all minions with 5 or more Attack.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()