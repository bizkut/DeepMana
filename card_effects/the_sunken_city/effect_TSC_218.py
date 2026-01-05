"""Effect for Lady S'theno (TSC_218).

Card Text: [x]<b>Immune</b> while attacking.
After you cast a spell, attack
the lowest Health enemy.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)