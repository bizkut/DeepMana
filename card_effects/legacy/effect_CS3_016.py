"""Effect for Reckoning (CS3_016).

Card Text: <b>Secret:</b> After an enemy minion deals 3 or more damage, destroy it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)