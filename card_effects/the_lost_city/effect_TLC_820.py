"""Effect for Glade Ecologist (TLC_820).

Card Text: [x]<b>Deathrattle:</b> Get a 1-Cost
Holy spell that gives a
minion +2 or -2 Health.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)