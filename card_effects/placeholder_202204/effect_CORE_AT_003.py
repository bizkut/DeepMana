"""Effect for Fallen Hero (CORE_AT_003).

Card Text: Your Hero Power deals 1 extra damage.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)