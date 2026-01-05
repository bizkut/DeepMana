"""Effect for Shadow Word: Devour (AV_324).

Card Text: Choose a minion.
It steals 1 Health from
 ALL other minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)