"""Effect for Libram of Justice (BT_011).

Card Text: Equip a 1/4 weapon. Change the Health of all enemy minions to 1.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)