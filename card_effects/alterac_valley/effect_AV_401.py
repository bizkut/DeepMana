"""Effect for Stormpike Quartermaster (AV_401).

Card Text: After you cast a spell,
give a random minion in your hand +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1