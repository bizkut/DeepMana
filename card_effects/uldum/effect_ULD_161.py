"""Effect for Neferset Thrasher (ULD_161).

Card Text: Whenever this attacks, deal 3 damage to your hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)