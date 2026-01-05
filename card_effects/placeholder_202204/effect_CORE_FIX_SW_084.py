"""Effect for Bloodbound Imp (CORE_FIX_SW_084).

Card Text: Whenever this attacks, deal 2 damage to your hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)