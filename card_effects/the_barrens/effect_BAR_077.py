"""Effect for Kargal Battlescar (BAR_077).

Card Text: [x]<b>Battlecry:</b> Summon a
5/5 Lookout for each
Watch Post you've
  summoned this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BAR_077t")