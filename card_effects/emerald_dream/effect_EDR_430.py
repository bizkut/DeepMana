"""Effect for Aessina (EDR_430).

Card Text: [x]<b>Battlecry:</b> If 20 friendly
minions have died this game,
deal 20 damage split among
all enemies.@ <i>({0} left!)</i>@ <i>(Ready!)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 20, source)