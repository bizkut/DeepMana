"""Effect for Baron Geddon (VAN_EX1_249).

Card Text: At the end of your turn, deal 2 damage to ALL other characters.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)