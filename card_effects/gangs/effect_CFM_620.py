"""Effect for Potion of Polymorph (CFM_620).

Card Text: <b>Secret:</b> After your opponent plays a minion, transform it into a
1/1 Sheep.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass