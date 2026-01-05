"""Effect for The Beast Within (TRL_119).

Card Text: Give a friendly Beast +1/+1, then it attacks a random enemy minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1