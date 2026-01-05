"""Effect for Lightforged Zealot (DRG_232).

Card Text: <b>Battlecry:</b> If your deck has no Neutral cards, equip a   4/2 Truesilver Champion. 
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass