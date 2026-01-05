"""Effect for Power Word: Glory (AT_013).

Card Text: Choose a minion. Whenever it attacks, restore 4 Health to
your hero.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 4, source)