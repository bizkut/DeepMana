"""Effect for Happy Ghoul (CORE_ICC_700).

Card Text: Costs (0) if your hero was healed this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 0, source)