"""Effect for Sanctum Spellbender (RLK_677).

Card Text: [x]Whenever your opponent
targets another minion with
a spell, redirect it to this.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass