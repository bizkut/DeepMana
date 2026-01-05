"""Effect for Totally Totems (WON_091).

Card Text: Summon all FIVE<i>?!</i> basic Totems.
<b>Overload:</b> (1)
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "WON_091t")