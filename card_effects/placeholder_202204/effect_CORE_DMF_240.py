"""Effect for Lothraxion the Redeemed (CORE_DMF_240).

Card Text: [x]<b>Battlecry:</b> For the rest of the
game, after you summon
a Silver Hand Recruit,
give it <b>Divine Shield</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_DMF_240t")