"""Effect for Adorable Infestation (SCH_617).

Card Text: Give a minion +1/+1. Summon a 1/1 Cub. Add a Cub to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SCH_617t")