"""Effect for Temple Enforcer (EX1_623).

Card Text: <b>Battlecry:</b> Give a friendly minion +3 Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 3, source)