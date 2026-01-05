"""Effect for Jan'alai, the Dragonhawk (TRL_316).

Card Text: [x]<b>Battlecry:</b> If your Hero Power
dealt 8 damage this game,
summon Ragnaros the
Firelord.@ <i>({0} left!)</i>@ <i>(Ready!)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 8, source)