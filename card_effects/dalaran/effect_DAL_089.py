"""Effect for Spellbook Binder (DAL_089).

Card Text: <b>Battlecry:</b> If you have <b>Spell Damage</b>, draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)