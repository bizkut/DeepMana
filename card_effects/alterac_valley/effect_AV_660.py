"""Effect for Iceblood Garrison (AV_660).

Card Text: [x]At the end of your turn,
deal $1 damage to all 
minions. Lasts 3 turns.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)