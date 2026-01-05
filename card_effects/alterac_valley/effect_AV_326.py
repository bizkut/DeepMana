"""Effect for Luminous Geode (AV_326).

Card Text: After a friendly minion is healed, give it +2 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 2, source)