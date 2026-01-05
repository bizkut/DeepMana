"""Effect for Vicious Scraphound (DAL_759).

Card Text: Whenever this minion
deals damage, gain that much Armor.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)