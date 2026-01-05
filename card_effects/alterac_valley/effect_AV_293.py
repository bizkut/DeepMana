"""Effect for Wing Commander Mulverick (AV_293).

Card Text: [x]<b>Rush</b>. Your minions have
"<b>Honorable Kill:</b> Summon a 
2/2 Wyvern with <b>Rush</b>."
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "AV_293t")