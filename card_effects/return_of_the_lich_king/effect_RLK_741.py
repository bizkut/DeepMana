"""Effect for Soulstealer (RLK_741).

Card Text: [x]<b>Battlecry:</b> Destroy all other
minions. Gain 1 <b>Corpse</b> for
each enemy destroyed.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()