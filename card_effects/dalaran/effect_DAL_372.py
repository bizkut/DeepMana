"""Effect for Arcane Fletcher (DAL_372).

Card Text: [x]Whenever you play a
1-Cost minion, draw a
spell from your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)