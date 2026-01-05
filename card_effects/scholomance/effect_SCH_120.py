"""Effect for Cabal Acolyte (SCH_120).

Card Text: [x]<b>Taunt</b>
<b>Spellburst:</b> Gain control
of a random enemy minion
with 2 or less Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass