"""Effect for Swift Messenger (GIL_528).

Card Text: [x]<b>Rush</b>
Each turn this is in your hand,
swap its Attack and Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)