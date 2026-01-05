"""Effect for Neferset Ritualist (ULD_196).

Card Text: <b>Battlecry:</b> Restore adjacent minions to full Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)