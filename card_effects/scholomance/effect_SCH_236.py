"""Effect for Diligent Notetaker (SCH_236).

Card Text: <b>Spellburst:</b> Return the spell to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass