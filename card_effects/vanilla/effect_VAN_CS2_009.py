"""Effect for Mark of the Wild (VAN_CS2_009).

Card Text: Give a minion <b>Taunt</b> and +2/+2.<i>
(+2 Attack/+2 Health)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 2, source)