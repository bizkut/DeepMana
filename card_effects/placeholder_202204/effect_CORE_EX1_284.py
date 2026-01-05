"""Effect for Azure Drake (CORE_EX1_284).

Card Text: <b>Spell Damage +1</b>
<b>Battlecry:</b> Draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)