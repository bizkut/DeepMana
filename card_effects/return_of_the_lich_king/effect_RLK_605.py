"""Effect for Blazing Power (RLK_605).

Card Text: [x]Give a minion +1/+1.
Repeat for each damaged
friendly character.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1