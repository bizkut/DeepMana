"""Effect for Grave Strength (RLK_Prologue_RLK_707).

Card Text: [x]Give your minions +1 Attack. Spend 5 <b>Corpses</b> to give them +3 instead.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
