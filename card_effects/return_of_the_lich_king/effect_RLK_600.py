"""Effect for Sunfire Smithing (RLK_600).

Card Text: Equip a 4/2 Sword.
Give a random minion
in your hand +4/+2.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 4
        target._max_health += 4