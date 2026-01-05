"""Effect for Libram of Hope (BT_024).

Card Text: Restore 8 Health. Summon an 8/8 Guardian with <b>Taunt</b> and <b>Divine Shield</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BT_024t")