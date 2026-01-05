"""Effect for Blood Crusader (RLK_927).

Card Text: [x]<b>Battlecry:</b> Your next Paladin
minion this turn costs 
Health instead of Mana.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)