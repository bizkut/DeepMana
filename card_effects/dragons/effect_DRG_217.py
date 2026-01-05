"""Effect for Dragon's Pack (DRG_217).

Card Text: Summon two 2/3 Spirit Wolves with <b>Taunt</b>. If you've <b>Invoked</b> twice, give them +3/+3.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DRG_217t")