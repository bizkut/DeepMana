"""Effect for Twilight Influence (EDR_463).

Card Text: <b>Choose One -</b> Destroy a minion with 3 or less Attack; or Summon a random 2-Cost minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "EDR_463t")