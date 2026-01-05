"""Effect for Greater Spinel Spellstone (TOY_825t2).

Card Text: Give Undead in your hand +3/+3.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
