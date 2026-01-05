"""Effect for Totemic Evidence (CORE_MAW_003).

Card Text: Choose a basic Totem and summon it.
<b>Infuse (3 Totems):</b>
Summon all 4 instead.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_MAW_003t")