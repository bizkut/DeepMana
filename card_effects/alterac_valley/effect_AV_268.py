"""Effect for Wildpaw Cavern (AV_268).

Card Text: [x]At the end of your
turn, summon a 3/4
Elemental that <b>Freezes</b>.
Lasts 3 turns.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "AV_268t")