"""Effect for Wilted Shadow (TLC_821).

Card Text: [x]<b>Lifesteal</b>
Whenever you heal an
enemy, this attacks it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)