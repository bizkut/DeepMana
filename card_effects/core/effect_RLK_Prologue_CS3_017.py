"""Effect for Gan'arg Glaivesmith (RLK_Prologue_CS3_017).

Card Text: <b>Outcast:</b> Give your hero +3 Attack this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Give +3/+0 and keywords
    if target:
        pass
        
target._attack += 3