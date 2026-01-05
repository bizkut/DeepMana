"""Effect for Electrowright (BOT_550).

Card Text: <b>Battlecry:</b> If you're holding a spell that costs (5) or more, gain +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 5
        target._max_health += 5