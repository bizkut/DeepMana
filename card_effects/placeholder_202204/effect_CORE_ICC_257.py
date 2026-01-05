"""Effect for Corpse Raiser (CORE_ICC_257).

Card Text: [x]<b>Battlecry:</b> Give a friendly
minion "<b>Deathrattle:</b>
  Resummon this minion."
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_ICC_257t")


def deathrattle(game, source):
    pass