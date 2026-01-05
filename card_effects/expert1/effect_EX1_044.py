"""Effect for Questing Adventurer (EX1_044).

Card Text: Whenever you play a card, gain +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1