"""Effect for Young Priestess (EX1_004).

Card Text: At the end of your turn, give another random friendly minion +1 Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)