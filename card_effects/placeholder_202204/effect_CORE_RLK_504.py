"""Effect for Corpse Bride (CORE_RLK_504).

Card Text: [x]<b>Battlecry:</b> Spend up to 10
 <b>Corpses</b> to summon a Risen 
Groom with <b>Taunt</b> and that
 much Attack and Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_RLK_504t")