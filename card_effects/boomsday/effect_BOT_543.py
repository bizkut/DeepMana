"""Effect for Omega Mind (BOT_543).

Card Text: [x]<b>Battlecry:</b> If you have 10
Mana Crystals, your spells
 have <b>Lifesteal</b> this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass