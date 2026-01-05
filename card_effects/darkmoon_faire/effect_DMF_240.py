"""Effect for Lothraxion the Redeemed (DMF_240).

Card Text: [x]<b>Battlecry:</b> For the rest of the
game, after you summon
a Silver Hand Recruit,
give it <b>Divine Shield</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DMF_240t")