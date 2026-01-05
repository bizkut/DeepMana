"""Effect for Survival of the Fittest (SCH_609).

Card Text: Give +4/+4 to all minions in your hand, deck, and battlefield.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 4
        target._max_health += 4