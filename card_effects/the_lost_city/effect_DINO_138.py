"""Effect for Diabolus Rex (DINO_138).

Card Text: <b>Kindred:</b> Deal 6 damage to your opponent's left and right-most minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 6, source)