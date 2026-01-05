"""Effect for Bob the Bartender (BG31_BOB).

Card Text: [x]<b>Battlecry:</b> Choose an action from the Battlegrounds!
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
