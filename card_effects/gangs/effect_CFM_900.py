"""Effect for Unlicensed Apothecary (CFM_900).

Card Text: After you summon a minion, deal 5 damage to your hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 5, source)