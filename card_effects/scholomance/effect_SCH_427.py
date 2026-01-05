"""Effect for Lightning Bloom (SCH_427).

Card Text: Refresh 2 Mana Crystals.
<b>Overload:</b> (2)
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass