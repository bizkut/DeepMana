"""Effect for Convincing Disguise (CORE_REV_920).

Card Text: [x]Transform a friendly minion
into one that costs (2) more.
<b>Infuse (4):</b> Transform all
friendly minions instead.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass