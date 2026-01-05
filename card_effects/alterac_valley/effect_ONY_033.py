"""Effect for Impfestation (ONY_033).

Card Text: Summon a 3/3
Dread Imp to attack each enemy minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "ONY_033t")