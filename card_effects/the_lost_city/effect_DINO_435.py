"""Effect for Crater Experiment (DINO_435).

Card Text: <b>Kindred:</b> Summon a
copy of this.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DINO_435t")