"""Effect for Hemet, Jungle Hunter (UNG_840).

Card Text: <b>Battlecry:</b> Destroy all cards in your deck that cost (3) or less.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()