"""Effect for Lady Naz'jar (TID_709).

Card Text: [x]While in your hand, this
   transforms after you cast a   
Fire, Frost, or Arcane spell.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass