"""Effect for Rock Bottom (TSC_925).

Card Text: [x]Summon a 1/1
Murloc, then <b>Dredge</b>.
If it's also a Murloc,
summon one more.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TSC_925t")