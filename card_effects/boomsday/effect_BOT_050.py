"""Effect for Rusty Recycler (BOT_050).

Card Text: <b>Taunt</b>
<b>Lifesteal</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass