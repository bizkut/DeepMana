"""Effect for Omega Devastator (DAL_770).

Card Text: [x]<b>Battlecry:</b> If you have 10
Mana Crystals, deal 10
damage to a minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 10, source)