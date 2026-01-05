"""Effect for Wither (RLK_655).

Card Text: [x]Choose a minion. Each
friendly Undead steals 1
Attack and Health from it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)