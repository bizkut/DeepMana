"""Effect for Windfury (CORE_CS2_039).

Card Text: Give a minion <b>Windfury</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1