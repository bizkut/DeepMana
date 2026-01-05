"""Effect for Freezing Trap (EX1_611).

Card Text: <b>Secret:</b> When an enemy minion attacks, return it to its owner's hand. It costs (2) more.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass