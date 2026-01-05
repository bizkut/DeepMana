"""Effect for Spirit Healer (BAR_744).

Card Text: After you cast a Holy spell, give a random friendly minion +2 Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 2, source)