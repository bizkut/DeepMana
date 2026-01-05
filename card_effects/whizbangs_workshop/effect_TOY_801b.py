"""Effect for Seedling Growth (TOY_801b).

Card Text: Gain <b>Spell Damage +1</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
