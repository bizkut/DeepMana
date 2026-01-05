"""Effect for Black Cat (GIL_838).

Card Text: <b>Spell Damage +1</b>
 <b>Battlecry:</b> If your deck has only odd-Cost cards, draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)