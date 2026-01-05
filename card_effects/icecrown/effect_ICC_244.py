"""Effect for Desperate Stand (ICC_244).

Card Text: Give a minion "<b>Deathrattle:</b> Return this to life with 1 Health."
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)