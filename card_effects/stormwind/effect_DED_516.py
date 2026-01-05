"""Effect for Deepwater Evoker (DED_516).

Card Text: [x]<b>Battlecry:</b> Draw a spell.
Gain Armor equal to
its Cost.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)