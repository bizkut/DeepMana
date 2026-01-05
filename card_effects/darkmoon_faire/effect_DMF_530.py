"""Effect for Feat of Strength (DMF_530).

Card Text: Give a random <b>Taunt</b> minion in your hand +5/+5.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 5
        target._max_health += 5