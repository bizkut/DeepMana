"""Effect for Gift of Luminance (SCH_302).

Card Text: Give a minion <b>Divine Shield</b>, then summon a 1/1 copy of it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SCH_302t")