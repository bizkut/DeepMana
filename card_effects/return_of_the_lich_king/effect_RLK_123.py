"""Effect for Bone Flinger (RLK_123).

Card Text: [x]<b>Battlecry:</b> If a friendly
Undead died after your last
turn, deal 2 damage.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)