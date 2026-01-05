"""Effect for Shoulder Check (ONY_025).

Card Text: <b>Tradeable</b>
Give a minion +2/+1 and <b>Rush</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2