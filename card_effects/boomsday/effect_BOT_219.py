"""Effect for Extra Arms (BOT_219).

Card Text: [x]Give a minion +2/+2.
Add 'More Arms!' to your
hand that gives +2/+2.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2