"""Effect for Hidden Cache (CFM_026).

Card Text: <b>Secret:</b> After your opponent plays a minion, give a random minion in your hand +2/+2.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2