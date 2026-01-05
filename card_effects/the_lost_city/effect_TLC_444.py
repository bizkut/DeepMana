"""Effect for Story of Galvadon (TLC_444).

Card Text: Give a minion three random <b>Bonus Effects</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1