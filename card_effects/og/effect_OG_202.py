"""Effect for Mire Keeper (OG_202).

Card Text: [x]<b>Choose One -</b> Summon a
2/2 Slime; or Gain an
empty Mana Crystal.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "OG_202t")