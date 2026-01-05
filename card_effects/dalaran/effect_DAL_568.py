"""Effect for Lightforged Blessing (DAL_568).

Card Text: <b>Twinspell</b>
Give a friendly minion <b>Lifesteal</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1