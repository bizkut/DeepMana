"""Effect for Mark of Nature (VAN_EX1_155).

Card Text: <b>Choose One -</b> Give a minion +4 Attack; or +4 Health and <b>Taunt</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 4, source)