"""Effect for Repentance (EX1_379).

Card Text: <b>Secret:</b> After your opponent plays a minion, reduce its Health to 1.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)