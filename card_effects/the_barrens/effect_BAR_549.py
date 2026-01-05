"""Effect for Mark of the Spikeshell (BAR_549).

Card Text: Give a minion +2/+2.
If it has <b>Taunt</b>, add a copy of it to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2