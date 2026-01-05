"""Effect for Blackwing Corruptor (BRM_034).

Card Text: <b>Battlecry:</b> If you're holding a Dragon, deal 5 damage.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 5, source)