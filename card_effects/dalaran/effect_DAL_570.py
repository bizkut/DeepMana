"""Effect for Never Surrender! (DAL_570).

Card Text: <b>Secret:</b> When your opponent casts a spell, give your minions +2 Health.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 2, source)