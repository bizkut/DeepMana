"""Effect for Party Favor Totem (CORE_REV_935).

Card Text: [x]At the end of your turn, 
summon a random basic 
Totem. <b>Infuse (2):</b> 
Summon two instead.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_REV_935t")