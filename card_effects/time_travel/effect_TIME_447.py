"""Effect for Power Word: Barrier (TIME_447).

Card Text: Give a character <b>Divine Shield</b>. Give minions in your hand +2 Health.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 2, source)