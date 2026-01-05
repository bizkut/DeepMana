"""Effect for Skulking Geist (CORE_ICC_701).

Card Text: <b>Battlecry:</b> Destroy all
1-Cost spells in both hands and decks.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()