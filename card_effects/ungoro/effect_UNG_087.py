"""Effect for Bittertide Hydra (UNG_087).

Card Text: Whenever this minion takes damage, deal 3 damage to your hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)