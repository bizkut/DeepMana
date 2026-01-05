"""Effect for Sweeping Strikes (DAL_062).

Card Text: Give a minion "Also damages minions next to whomever this attacks."
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1