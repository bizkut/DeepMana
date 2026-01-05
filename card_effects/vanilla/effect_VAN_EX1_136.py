"""Effect for Redemption (VAN_EX1_136).

Card Text: <b>Secret:</b> When a friendly minion dies, return it to life with 1 Health.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)