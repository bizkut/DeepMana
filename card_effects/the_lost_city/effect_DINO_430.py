"""Effect for Beast Speaker Taka (DINO_430).

Card Text: [x]<b>Battlecry:</b> <b>Discover</b> a
   <b>Legendary</b> Beast from any   
 class to gain its stats.
  <b>Deathrattle:</b> Summon it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DINO_430t")


def deathrattle(game, source):
    pass