"""Effect for Saruun (GDB_304).

Card Text: [x]<b>Battlecry:</b> Give all Elementals in your deck  <b>Fire Spell Damage +1</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
