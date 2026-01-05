"""Effect for Forest Warden Omu (SCH_614).

Card Text: <b>Spellburst:</b> Refresh your Mana Crystals.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass