"""Effect for Provoke (SW_023).

Card Text: [x]<b>Tradeable</b>
Choose a friendly minion.
Enemy minions attack it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass