"""Effect for Frostweave Dungeoneer (WC_805).

Card Text: [x]<b>Battlecry:</b> Draw a spell.
If it's a Frost spell,
summon two 1/1
   Elementals that <b>Freeze</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)