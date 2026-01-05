"""Effect for Witchwood Piper (GIL_584).

Card Text: [x]<b>Battlecry:</b> Draw the lowest
Cost minion from your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)