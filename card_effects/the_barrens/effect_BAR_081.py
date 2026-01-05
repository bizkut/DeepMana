"""Effect for Southsea Scoundrel (BAR_081).

Card Text: <b>Battlecry:</b> <b>Discover</b> a card in your opponent's deck. They draw theirs as well.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)