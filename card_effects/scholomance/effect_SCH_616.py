"""Effect for Twilight Runner (SCH_616).

Card Text: <b>Stealth</b>
Whenever this attacks, draw 2 cards.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)