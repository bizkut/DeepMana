"""Effect for All Fel Breaks Loose (CORE_MAW_012).

Card Text: [x]Summon a friendly Demon
that died this game.
<b>Infuse (3 Demons):</b>
Summon three instead.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_MAW_012t")