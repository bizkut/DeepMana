"""Effect for Murloc Holmes (REV_022).

Card Text: [x]<b>Battlecry:</b> Solve 3 Clues 
about your opponent's cards 
to get copies of them.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass