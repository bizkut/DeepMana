"""Effect for Forgotten Millennium (TIME_615).

Card Text: Fill your hand with random Undead.
They cost Health instead of Mana this turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)