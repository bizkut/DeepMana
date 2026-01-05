"""Effect for Drakkari Trickster (TRL_527).

Card Text: [x]<b>Battlecry:</b> Give each player a
copy of a random card from
their opponent's deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1