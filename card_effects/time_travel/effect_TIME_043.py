"""Effect for PMM Infinitizer (TIME_043).

Card Text: <b>Battlecry:</b> Set a friendly minion's Attack and Health to 8. It can't attack heroes this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 8, source)