"""Effect for Eredar Skulker (GDB_870).

Card Text: [x]<b>Combo and <b>Spellburst</b>:</b> Gain +2 Attack and <b>Stealth</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
