"""Effect for Ringmaster's Baton (DMF_524).

Card Text: After your hero attacks, give a Mech, Dragon, and Pirate in your hand +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1