"""Effect for Apotheosis (BT_257).

Card Text: Give a minion +2/+3 and <b>Lifesteal</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2