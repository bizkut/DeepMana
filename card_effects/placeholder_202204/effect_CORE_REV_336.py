"""Effect for Plot of Sin (CORE_REV_336).

Card Text: [x]Summon two 2/2 
Treants. <b>Infuse (5):</b> Two 
5/5 Ancients instead.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_REV_336t")