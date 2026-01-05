"""Effect for Crater Gator (TLC_250).

Card Text: [x]<b>Battlecry:</b> Until the start of
your next turn, the enemy
hero can't be healed.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)