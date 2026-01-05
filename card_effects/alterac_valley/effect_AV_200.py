"""Effect for Magister Dawngrasp (AV_200).

Card Text: [x]<b>Battlecry:</b> Recast a
spell from each spell
school you've cast
 this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass