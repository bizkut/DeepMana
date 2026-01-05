"""Effect for Zul'Drak Ritualist (DRG_064).

Card Text: [x]<b>Taunt</b>
 <b>Battlecry:</b> Summon three
random 1-Cost minions
for your opponent.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DRG_064t")