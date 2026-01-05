"""Effect for Dark Cultist (FP1_023).

Card Text: <b>Deathrattle:</b> Give a random friendly minion +3 Health.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 3, source)