"""Effect for Meat Grinder (RLK_120).

Card Text: <b>Battlecry:</b> Shred a random minion in your deck to gain 4 <b>Corpses.</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass