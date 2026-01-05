"""Effect for Shifty Sophomore (SCH_234).

Card Text: <b>Stealth</b>
<b>Spellburst:</b> Add a <b>Combo</b> card to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass