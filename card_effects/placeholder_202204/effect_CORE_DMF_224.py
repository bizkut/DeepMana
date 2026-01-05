"""Effect for Expendable Performers (CORE_DMF_224).

Card Text: Summon seven 1/1 Illidari with <b>Rush</b>. If they all die this turn, summon seven more.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_DMF_224t")