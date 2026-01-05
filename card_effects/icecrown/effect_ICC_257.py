"""Effect for Corpse Raiser (ICC_257).

Card Text: [x]<b>Battlecry:</b> Give a friendly
minion "<b>Deathrattle:</b>
  Resummon this minion."
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "ICC_257t")


def deathrattle(game, source):
    pass