"""Effect for Guidance (YOP_024).

Card Text: Look at two spells. Add one to your hand or <b>Overload:</b> (1) to get both.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass