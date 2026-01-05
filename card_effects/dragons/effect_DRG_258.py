"""Effect for Sanctuary (DRG_258).

Card Text: [x]<b>Sidequest:</b> Take no
damage for a turn.
<b>Reward:</b> Summon a 3/6
minion with <b>Taunt</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DRG_258t")