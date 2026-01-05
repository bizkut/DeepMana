"""Effect for Sigil of Silence (BAR_705).

Card Text: At the start of your
next turn, <b>Silence</b> all
enemy minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.silence(target)