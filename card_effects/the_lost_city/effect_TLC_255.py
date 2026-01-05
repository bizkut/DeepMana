"""Effect for Crystal Tender (TLC_255).

Card Text: [x]<b>Tradeable</b>
<b>Battlecry:</b> Gain empty Mana
Crystals until both players
have the same Mana.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass