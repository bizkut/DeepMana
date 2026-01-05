"""Effect for Doggie Biscuit (DED_009).

Card Text: [x]<b>Tradeable</b>
Give a minion +2/+3.
After you <b>Trade</b> this, give
a friendly minion <b>Rush</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2