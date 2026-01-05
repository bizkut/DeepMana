"""Effect for Ravasaur Matriarch (TLC_825).

Card Text: [x]<b>Kindred:</b> Deal damage to
an enemy minion equal to
this minion's Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)