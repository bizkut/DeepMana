"""Effect for Shadowblade Slinger (DED_503).

Card Text: [x]<b>Battlecry:</b> If you've taken
damage this turn, deal that
 much to an enemy minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)