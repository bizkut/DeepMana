"""Effect for Riot! (CORE_REV_337).

Card Text: [x]Your minions can't be 
reduced below 1 Health 
this turn. They each attack 
a random enemy minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)