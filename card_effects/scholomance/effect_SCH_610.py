"""Effect for Guardian Animals (SCH_610).

Card Text: Summon two Beasts that cost (5) or less from your deck. Give them <b>Rush</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SCH_610t")