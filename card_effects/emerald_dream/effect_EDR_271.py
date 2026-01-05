"""Effect for Grove Shaper (EDR_271).

Card Text: [x]After you cast a Nature spell,
summon a 2/2 Treant with
"<b>Deathrattle:</b> Get a copy
of that spell."
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "EDR_271t")