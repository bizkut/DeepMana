"""Effect for Noxious Infiltrator (RLK_529).

Card Text: [x]<b>Poisonous</b>
<b>Battlecry:</b> If a friendly Undead
died after your last turn, deal 1
damage to a minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)