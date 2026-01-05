"""Effect for Resplendent Dreamweaver (EDR_860).

Card Text: [x]<b>Lifesteal</b>
<b>Battlecry:</b> If you've <b>Imbued</b>
your Hero Power twice, deal
4 damage to a minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 4, source)