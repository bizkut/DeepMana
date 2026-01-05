"""Effect for Tinker's Sharpsword Oil (GVG_022).

Card Text: Give your weapon +3 Attack. <b>Combo:</b> Give a random friendly minion +3 Attack.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3