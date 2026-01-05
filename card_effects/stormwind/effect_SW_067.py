"""Effect for Stockades Guard (SW_067).

Card Text: [x]<b>Battlecry:</b> Give a
friendly minion <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1