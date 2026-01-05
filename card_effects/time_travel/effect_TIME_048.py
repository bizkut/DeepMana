"""Effect for Clockwork Rager (TIME_048).

Card Text: [x]<b>Battlecry:</b> Gain +1 Health
for each turn you've taken
this game.@ <i>(@ turns)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)