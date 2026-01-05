"""Effect for Commencement (SCH_533).

Card Text: Summon a minion from your deck. Give it <b>Taunt</b> and <b>Divine Shield</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SCH_533t")