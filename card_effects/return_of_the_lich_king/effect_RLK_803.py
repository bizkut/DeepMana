"""Effect for Grand Magister Rommath (RLK_803).

Card Text: [x]<b>Battlecry:</b> Recast each spell
you've cast this game that
didn't start in your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass