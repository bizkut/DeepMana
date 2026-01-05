"""Effect for Tuskarr Jouster (AT_104).

Card Text: <b>Battlecry:</b> Reveal a minion in each deck. If yours costs more, restore #7 Health to your hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 7, source)