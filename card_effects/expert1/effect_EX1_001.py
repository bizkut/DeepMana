"""Effect for Lightwarden (EX1_001).

Card Text: Whenever a character is healed, gain +2 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 2, source)