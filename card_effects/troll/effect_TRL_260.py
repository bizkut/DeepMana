"""Effect for Bwonsamdi, the Dead (TRL_260).

Card Text: [x]<b>Battlecry:</b> Draw 1-Cost
minions from your deck
until your hand is full.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)