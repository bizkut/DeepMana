"""Effect for Harbinger Celestia (BOT_555).

Card Text: [x]<b>Stealth</b>
After your opponent plays
a minion, become a
copy of it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass