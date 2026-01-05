"""Effect for Mordresh Fire Eye (BAR_547).

Card Text: [x]<b>Battlecry:</b> If you've dealt 10
damage with your Hero Power
 this game, deal 10 damage
to all enemies.@ <i>({0} left!)</i>@ <i>(Ready!)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 10, source)