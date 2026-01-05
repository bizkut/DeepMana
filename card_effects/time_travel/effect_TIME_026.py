"""Effect for Entropic Continuity (TIME_026).

Card Text: [x]Give your minions +1/+1.
Shuffle 2 Shreds of Time
into your deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1