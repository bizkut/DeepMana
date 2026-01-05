"""Effect for Dragon Turtle (FIR_956).

Card Text: [x]<b>Battlecry:</b> If you're holding
a minion with a <b>Dark Gift</b>,
give your hero +3 Attack this
turn and 6 Armor.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3