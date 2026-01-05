"""Effect for Elemental Allies (DRG_324).

Card Text: [x]<b>Sidequest:</b> Play an
Elemental 2 turns in a row.
<b>Reward:</b> Draw 3 spells
from your deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)