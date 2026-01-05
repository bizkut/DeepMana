"""Effect for Iceblood Tower (AV_290).

Card Text: [x]At the end of your turn,
cast another spell from
your deck. Lasts 3 turns.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass