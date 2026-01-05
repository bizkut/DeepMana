"""Effect for Cho'gall (OG_121).

Card Text: [x]<b>Battlecry:</b> Return all cards
you discarded this game to
your hand. They cost Health
instead of Mana.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)