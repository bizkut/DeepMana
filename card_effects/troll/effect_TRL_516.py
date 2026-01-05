"""Effect for Gurubashi Offering (TRL_516).

Card Text: At the start of your turn, destroy this and gain 8 Armor.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()