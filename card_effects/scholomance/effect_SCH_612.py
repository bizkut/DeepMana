"""Effect for Runic Carvings (SCH_612).

Card Text: <b>Choose One -</b> Summon four 2/2 Treant Totems; or <b>Overload:</b> (2) to summon them with <b>Rush</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SCH_612t")