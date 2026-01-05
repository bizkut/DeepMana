"""Effect for Disruptive Spellbreaker (RLK_607).

Card Text: At the end of your turn, your
opponent discards a spell.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass