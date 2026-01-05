"""Effect for Malygos the Spellweaver (CS3_034).

Card Text: <b>Battlecry:</b> Draw spells until your hand is full.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)