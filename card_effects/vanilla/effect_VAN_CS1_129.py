"""Effect for Inner Fire (VAN_CS1_129).

Card Text: Change a minion's Attack to be equal to its Health.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)