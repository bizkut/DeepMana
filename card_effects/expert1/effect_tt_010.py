"""Effect for Spellbender (tt_010).

Card Text: <b>Secret:</b> When an enemy casts a spell on a minion, summon a 1/3 as the new target.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "tt_010t")