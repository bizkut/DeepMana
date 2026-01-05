"""Effect for Crowd Roaster (TRL_569).

Card Text: [x]<b>Battlecry:</b> If you're holding
a Dragon, deal 7 damage
to an enemy minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 7, source)