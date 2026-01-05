"""Effect for Criminal Lineup (CORE_REV_517).

Card Text: [x]Choose a friendly minion.
Summon 3 copies of it.
<b>Overload:</b> (2)
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_REV_517t")