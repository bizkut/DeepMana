"""Effect for Keeneye Spotter (RLK_827).

Card Text: [x]Whenever your hero
attacks a minion, set
its Health to 1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)