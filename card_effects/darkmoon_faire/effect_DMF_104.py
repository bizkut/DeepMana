"""Effect for Grand Finale (DMF_104).

Card Text: Summon an 8/8 Elemental. Repeat for each Elemental you played last turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DMF_104t")