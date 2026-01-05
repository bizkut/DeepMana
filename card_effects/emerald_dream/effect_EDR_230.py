"""Effect for Beanstalk Brute (EDR_230).

Card Text: <b>Battlecry:</b> Give +4/+4 to the top 3 minions in your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 4
        target._max_health += 4